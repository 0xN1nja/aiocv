"""
Eyes Detection Module
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
class EyesDetector():
    def __init__(self,img) -> None:
        self.img=img
    def findEyes(self,color=(255,0,0),thickness=2) -> "Image":
        """
        Detects Eyes On Image And Returns It
        color = (255,0,0) Format : (B,G,R)
        """
        self.eyeCascade=cv2.CascadeClassifier(fr"{path}\haarcascade_eye.xml")
        self.eyes=self.eyeCascade.detectMultiScale(self.img,1.1,4)
        for x,y,w,h in self.eyes:
            cv2.rectangle(self.img,(x,y),(x+w,y+h),color,thickness)
        return self.img