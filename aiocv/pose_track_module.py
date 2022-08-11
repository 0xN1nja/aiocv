"""
Pose Tracking Module
Author : Abhimanyu Sharma
Part Of AIOCV Module
GitHub : https://github.com/0xN1nja
"""
import cv2
import mediapipe as mp
import time
class PoseDetector():
    def __init__(self,mode=False,smooth=True,detectionConfidence=0.5,trackConfidence=0.5) -> None:
        """
        Default Mode : False
        Only Up Body : False
        Smooth : True
        Default Detection Confidence : 50%
        Default Tracking Confidence : 50%
        If You Are Not Getting Desired Results, Consider Changing self.detectionConfidence = 1 And self.trackConfidence = 1
        """
        self.mode=mode
        self.smooth=smooth
        self.detectionConfidence=detectionConfidence
        self.trackConfidence=trackConfidence
        self.mpDraw=mp.solutions.drawing_utils
        self.mpPose=mp.solutions.pose
        self.pose=self.mpPose.Pose(static_image_mode=self.mode,smooth_landmarks=self.smooth,min_detection_confidence=self.detectionConfidence,min_tracking_confidence=self.trackConfidence)
    def findPose(self,img,draw=True) -> "Image":
        """
        Draws The Landmarks Detected In img And Returns The img
        """
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        return img
    def getPosition(self,img,draw=False) -> "landmarkList":
        """
        Get x,y Cordinates Of Landmarks Detected On Image/Video
        Returns The 2D landmarkList Which Contains : [[id,x,y]] Of Landmarks
        """
        self.landmarkList=[]
        for id,lm in enumerate(self.results.pose_landmarks.landmark):
            h,w,c=img.shape
            cx,cy=int(lm.x*w),int(lm.y*h)
            self.landmarkList.append([id,cx,cy])
            if draw:
                cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
        return self.landmarkList