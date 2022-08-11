"""
QR Code Detection Module
Part Of AIOCV Module
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import cv2
import qrcode
import numpy as np
class QRCodeReader():
    def __init__(self,img) -> None:
        self.img=img
    def findQRCode(self,color=(255,0,0),thickness=3) -> "Text":
        """
        Detects QR Code, Draws Rectangle On Detected Code And Returns Data In It
        """
        self.qrReader=cv2.QRCodeDetector()
        self.text,points,_=self.qrReader.detectAndDecode(self.img)
        x,y=(int(points[0][0][0]),int(points[0][0][0])),(int(points[0][2][0]),int(points[0][2][0]))
        cv2.rectangle(self.img,x,y,color,thickness)
        return self.text