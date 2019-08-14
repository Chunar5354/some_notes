import socket
import threading
import struct
import cv2
import time
import os
import numpy

class webCamera: 
    def __init__(self, resolution = (640, 480), host = ('192.168.43.169', 7999)):      
        self.resolution = resolution
        self.host = host
        self.setSocket(self.host)
        self.img_quality = 15

    # set size
    def setImageResolution(self, resolution):      
        self.resolution = resolution

    # set ip and port
    def setHost(self, host):
        self.host = host

    # create socket object
    def setSocket(self, host):      
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)           
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)   
        self.socket.bind(self.host) 
        self.socket.listen(5)
        print("Server running on port:%d" % host[1]) 

    def _processConnection(self, client, addr):     
        # if(self.recv_config(client) == 0):        
        #    return    
        camera = cv2.VideoCapture(0)

        # willbe used in next method 'cv2.imencode()' 
        # IMWRITE_JPEG_QUALITY means save into JPEG form , and the quality is 'self.img_quality', here is 15
        # cv2.IMWRITE_JPEG_QUALITY must convert in 'int'
        # and this argument should create as a list
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), self.img_quality]


        while True:        
            time.sleep(0.13)
            grabbed, self.img = camera.read()

            # compress image
            self.img  = cv2.resize(self.img, (640, 480))

            # cv2.imencode(), argus: (ext(means form), image object, encode_param)
            # cv2.imencode() returns a tuple which has 2 elements
            # the first element is flag, a bool object, if this statement worked, returns True
            # the second element is a numpy.ndarray object
            result, imgencode = cv2.imencode('.jpg', self.img, encode_param)

            # img_code = numpy.array(imgencode)  # why numpy.array() ?
            self.imgdata = imgencode.tostring()

            try:                    
                client.send(struct.pack("lhh",len(self.imgdata),
                        640, 480) + self.imgdata)  # 发送图片信息(图片长度,分辨率,图片内容)                
            except:            
                print('failed')
                camera.release()                    
                return

    def run(self):      
        while True:        
            client, addr = self.socket.accept()
            clientThread = threading.Thread(target = self._processConnection, 
                args = (client, addr, ))  # 有客户端连接时产生新的线程进行处理                      
            clientThread.start()

def main():      
    cam = webCamera()    
    cam.run()

if __name__ == "__main__":
    main()
