"""
Hand Track Module
Part Of AIOCV Module
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import cv2
import mediapipe as mp
import time
class HandTrack():
    def __init__(self,mode=False,maxHands=2,detectionConfidence=0.5,trackConfidence=0.5) -> None:
        """
        If You Are Not Getting Desired Results, Consider Changing self.detectionConfidence = 1 And self.trackConfidence = 1
        If Your Image Has More Than 2 Hands, Set The maxHands To 10
        """
        self.mode=mode
        self.maxHands=maxHands
        self.detectionConfidence=detectionCon=0.5
        self.trackConfidence=trackConfidence=0.5
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(static_image_mode=self.mode,max_num_hands=self.maxHands,min_detection_confidence=self.detectionConfidence,min_tracking_confidence=self.trackConfidence)
        self.mpDraw=mp.solutions.drawing_utils
    def findHands(self,img,draw=True) -> "Image":
        """
        Draws The Landmarks On Hands
        """ 
        imgRgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRgb)
        if self.results.multi_hand_landmarks:
            for i in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,i,self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self,img,handNo=0,draw=True) -> list:
        """
        Returns The Landmarks List
        """
        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),3,(255,0,0),cv2.FILLED)
        return lmList