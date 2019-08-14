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
            if bufSize:           
                 try:                  
                    self.mutex.acquire()
                    self.buf = b''                
                    tempBuf = self.buf

                    while bufSize:                 #循环读取到一张图片的长度
                        tempBuf = self.socket.recv(bufSize)   # 这里要读9172个字节，但是读到的实际tempBUf长度为6260
                        bufSize -= len(tempBuf)
                        self.buf += tempBuf
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

    def getData(self):            
        showThread = threading.Thread(target=self._processImage)
        showThread.start()


def main():    
    print("创建连接...")    
    cam = webCamConnect()
    print("像素为:%d * %d"%(cam.resolution[0],cam.resolution[1]))    
    print("目标ip为%s:%d"%(cam.remoteAddress[0],cam.remoteAddress[1])) 
    cam.connect()
    cam.getData()

if __name__ == "__main__":      
    main()