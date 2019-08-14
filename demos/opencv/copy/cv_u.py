import socket
import threading
import struct
import os
import time
import sys
import numpy
import cv2
import re


class webCamConnect():      
    def __init__(self, resolution = [640,480],
                       remoteAddress = ("192.168.43.169", 7999),
                       windowName = "video"):          
        self.remoteAddress = remoteAddress  # connect with socket
        self.resolution = resolution  # change size
        self.name = windowName
        self.mutex = threading.Lock()
        self.src = 911 + 15        
        self.interval = 0
        self.path = os.getcwd()        
        self.img_quality = 15

    # cerate socket object
    def _setSocket(self):      
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.SO_REUSEADDR:当socket关闭后，本地端用于该socket的端口号立刻就可以被重用
        # 1表示将 socket.SO_REUSEADDR 设置为 True
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # connect to server
    def connect(self):      
        self._setSocket()
        self.socket.connect(self.remoteAddress)

    def _processImage(self):
        # struct.pack() returns a 'bytes' object
        # the format string 'llh' means the after 3 arguments as ('long', 'short', 'short') type
        # do this 'self.socket.send' can customsize quality and size
        self.socket.send(struct.pack("lhh", self.src, self.resolution[0], self.resolution[1]))
        
        while True:        
            info = struct.unpack("lhh", self.socket.recv(8))
            bufSize = info[0]
            print('info 0:', info[0])
            if bufSize:           
                 try:                  
                    self.mutex.acquire()
                    self.buf = b''                
                    tempBuf = self.buf

                    while bufSize:                 #循环读取到一张图片的长度
                        print('bufSize here: ', bufSize)
                        tempBuf = self.socket.recv(bufSize)   # 这里要读9172个字节，但是读到的实际tempBUf长度为6260
                        bufSize -= len(tempBuf)
                        self.buf += tempBuf
                        print('bufSize: ', bufSize)
                        print('self.buf: ', type(self.buf))
                        data = numpy.frombuffer(self.buf, dtype='uint8')    # fromstring()
                        self.image = cv2.imdecode(data, 1)       # imdecode()   
                        cv2.imshow(self.name, self.image)            
                 except:                
                     print("接收失败")                
                     pass;              
                 finally:                
                     self.mutex.release();               
                     if cv2.waitKey(10) == 27:                    
                         self.socket.close()                    
                         cv2.destroyAllWindows()                    
                         print("放弃连接")                    
                         break

    def getData(self, interval):            
        showThread = threading.Thread(target=self._processImage)
        showThread.start()
        if interval != 0:   # 非0则启动保存截图到本地的功能  
            saveThread = threading.Thread(target=self._savePicToLocal,args = (interval, 
                ));          
            saveThread.setDaemon(1)   
            saveThread.start()

    def setWindowName(self, name):      
        self.name = name

    def setRemoteAddress(remoteAddress):      
        self.remoteAddress = remoteAddress

    def _savePicToLocal(self, interval):      
        while(1):          
            try:              
                self.mutex.acquire();              
                path = os.getcwd() + "\\" + "savePic"        
                if not os.path.exists(path):                  
                    os.mkdir(path)   
                cv2.imwrite(path + "\\" + time.strftime("%Y%m%d-%H%M%S", 
                        time.localtime(time.time())) + ".jpg",self.image)
            except:              
                pass     
            finally:              
                self.mutex.release()          
                time.sleep(interval)

    def check_config(self):    
        path=os.getcwd()
        print(path)

        if os.path.isfile(r'%s\video_config.txt' % path) is False:
            f = open("video_config.txt", 'w+')
            print("w = %d,h = %d" %(self.resolution[0], self.resolution[1]), file=f)
            print("IP is %s:%d" %(self.remoteAddress[0], self.remoteAddress[1]), file=f)
            print("Save pic flag:%d" %(self.interval), file=f)
            print("image's quality is:%d,range(0~95)"%(self.img_quality), file=f)
            f.close()        
            print("初始化配置")
        else:        
            f = open("video_config.txt", 'r+')        
            tmp_data = f.readline(50)                  # 1 resolution
            num_list = re.findall(r"\d+", tmp_data)        
            self.resolution[0] = int(num_list[0])        
            self.resolution[1] = int(num_list[1])        
            tmp_data = f.readline(50)                  # 2 ip, port        
            num_list = re.findall(r"\d+", tmp_data)        
            str_tmp = "%d.%d.%d.%d" % (int(num_list[0]), int(num_list[1]), int(num_list[2]), int(num_list[3]))
            self.remoteAddress = (str_tmp, int(num_list[4]))
            tmp_data = f.readline(50)                 # 3 savedata_flag
            self.interval = int(re.findall(r"\d", tmp_data)[0])
            tmp_data = f.readline(50)                 # 3 savedata_flag        
            # print(tmp_data)        
            self.img_quality = int(re.findall(r"\d+", tmp_data)[0]) 
            # print(self.img_quality)        
            self.src = 911 + self.img_quality
            f.close()
            print("读取配置")

def main():    
    print("创建连接...")    
    cam = webCamConnect()
    cam.check_config()    
    print("像素为:%d * %d"%(cam.resolution[0],cam.resolution[1]))    
    print("目标ip为%s:%d"%(cam.remoteAddress[0],cam.remoteAddress[1])) 
    cam.connect()
    cam.getData(cam.interval)

if __name__ == "__main__":      
    main()