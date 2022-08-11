"""
Contour Detection Module
Part Of AIOCV Module
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import cv2
import time
import mediapipe as mp
class ContourDetector():
    def __init__(self,img) -> None:
        self.img=img
    def findContours(self,drawOutline=True,drawName=True,drawRectangle=False,outlineColor=(255,0,0),rectangleColor=(255,0,0),thickness=3) -> "Image":
        """
        Detects Contours On img
        To Draw Outline On Shape : drawOutline=True
        To Draw Detected Shape Name : drawName=True
        To Draw Rectangle On Detected Contour : drawRectangle=True
        outlineColor=(255,0,0) Format : (B,G,R)
        rectangleColor=(255,0,0) Format : (B,G,R)
        thickness=3    
        """
        self.imgCanny=cv2.Canny(self.img,100,100)
        countours,_=cv2.findContours(self.imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for cnt in countours:
            self.area=cv2.contourArea(cnt)
            if self.area>500:
                self.perimeter=cv2.arcLength(cnt,closed=True)
                if drawOutline:
                    cv2.drawContours(self.img,cnt,-1,outlineColor,thickness)
                self.approx=cv2.approxPolyDP(cnt,0.02*self.perimeter,closed=True)
                corners=len(self.approx)
                x,y,w,h=cv2.boundingRect(self.approx)
                if corners==3:
                    shape="Triangle"
                elif corners==4:
                    shape="Quadrirateral"
                else:
                    shape="Circle/Oval"
                if drawRectangle:
                    cv2.rectangle(self.img,(x,y),(x+w,y+h),rectangleColor,thickness)
                if drawName:
                    cv2.putText(self.img,shape,(x+w//2-10,y+h//2-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
        return self.img