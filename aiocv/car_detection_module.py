"""
Car Detection Module
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
class CarDetector():
    def __init__(self,img) -> None:
        self.img=img
    def findCars(self,color=(255,0,0),thickness=2) -> "Image":
        """
        Detects Cars On Image And Returns It
        color = (255,0,0) Format : (B,G,R)
        thickness = 2 
        """
        self.carsCascade=cv2.CascadeClassifier(fr"{path}\haarcascade_car.xml")
        self.cars=self.carsCascade.detectMultiScale(self.img,1.1,4)
        for x,y,w,h in self.cars:
            cv2.rectangle(self.img,(x,y),(x+w,y+h),color,thickness)
        return self.img