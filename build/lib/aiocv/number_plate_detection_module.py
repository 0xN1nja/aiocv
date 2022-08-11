"""
Number Plate Detection Module
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
class NumberPlateDetector():
    def __init__(self,img) -> None:
        self.img=img
    def findNumberPlate(self,color=(255,0,0),thickness=2) -> "Image":
        """
        Detects Number Plate On Image And Returns It
        color = (255,0,0) Format : (B,G,R)
        """
        self.numberPlateCascade=cv2.CascadeClassifier(fr"{path}\haarcascade_russian_plate_number.xml")
        self.numberPlate=self.numberPlateCascade.detectMultiScale(self.img,1.1,4)
        for x,y,w,h in self.numberPlate:
            cv2.rectangle(self.img,(x,y),(x+w,y+h),color,thickness)
        return self.img