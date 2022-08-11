"""
Smile Detection Module
Part Of AIOCV Module
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import cv2
path=__file__.split("\\")
path.pop()
path.pop()
path.append("haarcascades")
path="\\".join(path)
class SmileDetector():
    def __init__(self,img) -> None:
        self.img=img
    def findSmile(self,color=(255,0,0),thickness=2) -> "Image":
        """
        Detects Smile On Image And Returns It
        color = (255,0,0) Format : (B,G,R)
        """
        self.smileCascade=cv2.CascadeClassifier(fr"{path}\haarcascade_smile.xml")
        self.smile=self.smileCascade.detectMultiScale(self.img,1.8,20)
        for x,y,w,h in self.smile:
            cv2.rectangle(self.img,(x,y),(x+w,y+h),color,thickness)
        return self.img