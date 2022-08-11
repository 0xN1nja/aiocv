"""
Face Mesh Module
Part Of AIOCV Module
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import cv2
import mediapipe as mp
import time
class FaceMesh():
    def __init__(self,staticMode=False,maxFaces=2,thickness=1,circle_radius=2,detectionConfidence=0.5,trackConfidence=0.5) -> None:
        """
        If You Are Not Getting Desired Results, Consider Changing self.detectionConfidence = 1 And self.trackConfidence = 1
        If Your Image Has More Than 2 Faces, Set The maxFaces To 10
        If You Want A Thicker Mesh, Set thickness = 2
        You Can Also Set The Circle Radius Drawn On The Image : circle_radius = 2
        """
        self.staticMode=staticMode
        self.maxFaces=maxFaces
        self.thickness=thickness
        self.circle_radius=circle_radius
        self.detectionConfidence=detectionConfidence
        self.trackConfidence=trackConfidence
        self.mpDraw=mp.solutions.drawing_utils
        self.mpFaceMesh=mp.solutions.face_mesh
        self.faceMesh=self.mpFaceMesh.FaceMesh(static_image_mode=self.staticMode,max_num_faces=self.maxFaces,min_detection_confidence=self.detectionConfidence,min_tracking_confidence=self.trackConfidence)
        self.drawSpec=self.mpDraw.DrawingSpec(thickness=self.thickness,circle_radius=self.circle_radius)
    def findFaceMesh(self,img,draw=True) -> "Image":
        """
        Draws The Mesh On The Landmarks And Returns It
        Also Returns The Landmark List
        """        
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.faceMesh.process(imgRGB)
        lmList=[]
        if self.results.multi_face_landmarks:
            for face in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,face,self.mpFaceMesh.FACEMESH_CONTOURS,self.drawSpec,self.drawSpec)
                for id,lm in enumerate(face.landmark):
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    lmList.append([id,cx,cy])
        return img,lmList