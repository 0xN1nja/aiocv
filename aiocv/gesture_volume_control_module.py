"""
Gesture Volume Control Module
Part Of AIOCV Module
Author : Abhimanyu Sharma
GitHub : https://github.com/0xN1nja
"""
import cv2
import time
import numpy as np
import aiocv
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
wCam, hCam = 640, 480
class GestureVolumeControl():
    def __init__(self,webcamIndex=0) -> None:
        self.webcamIndex=webcamIndex
    def controlVolume(self,color=(255,0,0),thickness=2) -> None:
        """
        Creates A Screen On Which You Can Control Volume Using Your Thumb And Index Finger
        """
        cap = cv2.VideoCapture(self.webcamIndex)
        cap.set(3, wCam)
        cap.set(4, hCam)
        pTime = 0
        detector = aiocv.HandTrack()
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volRange = volume.GetVolumeRange()
        minVol = volRange[0]
        maxVol = volRange[1]
        vol = 0
        volBar = 400
        volPer = 0
        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)
            if len(lmList) != 0:
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                cv2.circle(img, (x1, y1), 15,color, cv2.FILLED)
                cv2.circle(img, (x2, y2), 15,color, cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2),color, thickness)
                cv2.circle(img, (cx, cy), 15,color, cv2.FILLED)
                length = math.hypot(x2 - x1, y2 - y1)
                vol = np.interp(length, [50, 300], [minVol, maxVol])
                volBar = np.interp(length, [50, 300], [400, 150])
                volPer = np.interp(length, [50, 300], [0, 100])
                print(int(length), vol)
                volume.SetMasterVolumeLevel(vol, None)
                if length < 50:
                    cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
            cv2.rectangle(img, (50, 150), (85, 400),color, 3)
            cv2.rectangle(img, (50, int(volBar)), (85, 400),color, cv2.FILLED)
            cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,1,color, thickness)
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,1,color, thickness)
            cv2.imshow("Img", img)
            cv2.waitKey(1)