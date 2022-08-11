"""
Face Detection Module
Part Of AIOCV Module
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import cv2
import mediapipe as mp
import time
class FaceDetector():
    def __init__(self,detectionConfidence=0.5) -> None:
        """
        If You Are Not Getting Desired Results, Consider Changing self.detectionConfidence = 1 
        """
        self.detectionConfidence=detectionConfidence
        self.mpFaceDetection=mp.solutions.face_detection
        self.mpDraw=mp.solutions.drawing_utils
        self.faceDetection=self.mpFaceDetection.FaceDetection(self.detectionConfidence)
    def findFace(self,img,draw=True) -> list:
        """
        Detects The Face Landmarks In Image/Video
        Returns The Bounding Box List
        """
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.faceDetection.process(imgRGB)
        bboxs=[]
        if self.results.detections:
            for id,detection in enumerate(self.results.detections):
                bboxC=detection.location_data.relative_bounding_box
                h,w,c=img.shape
                bbox=int(bboxC.xmin*w),int(bboxC.ymin*h),\
                    int(bboxC.width*w),int(bboxC.height*h)
                bboxs.append([bbox,detection.score])
                if draw:
                    cv2.rectangle(img,bbox,(255,0,255),2) # Add Custom Color In (B,G,R) Format
                    cv2.putText(img,f"{int(detection.score[0]*100)}%",(bbox[0],bbox[1]-20),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2) # Add Custom Color In (B,G,R) Format
        return img,bboxs