# AIOCV

aiocv Is A Python Library Used To Track Hands, Track Pose, Detect Face, Detect Contours (Shapes), Detect Cars, Detect Number Plate, Detect Smile, Detect Eyes, Control Volume Using Gesture, Read QR Codes And Create Face Mesh On Image/Video.

## Installation

Use the package manager [pip](https://pypi.org/project/aiocv/) to install aiocv.

```bash
pip install aiocv
```

## Usage
#### Hand Tracking
```python
import aiocv
import cv2
img = cv2.imread("hands.png")
# Make An Object
hands = aiocv.HandTrack()
# Use findHands() Method To Track Hands On Image/Video
hands.findHands(img,draw=True)
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Params For findHands() Method :
```python
findHands(self,img=None,draw=True)
```
#### If You Are Not Getting Desired Results, Consider Changing detectionConfidence = 1 and trackConfidence = 1
#### Output :
![Hand Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example4.png)
#### Pose Detector
```python
import aiocv
import cv2
img = cv2.imread("man.png")
# Make An Object
pose = aiocv.PoseDetector()
# Use findPose() Method To Detect Pose On Image/Video
pose.findPose(img,draw=True)
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Params For findPose() Method :
```python
findPose(self,img=None,draw=True)
```
#### If You Are Not Getting Desired Results, Consider Changing detectionConfidence = 1 and trackConfidence = 1
#### Output :
![Pose Track Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example3.png)
#### Face Detection
```python
import aiocv
import cv2
img = cv2.imread("elon_musk.png")
# Make An Object
face = aiocv.FaceDetector()
# Use findFace() Method To Detect Face On Image/Video
face.findFace(img,draw=True)
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Params For findFace() Method :
```python
findFace(self,img=None,draw=True)
```
#### If You Are Not Getting Desired Results, Consider Changing detectionConfidence = 1
#### Output :
![Face Detection Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example1.png)
#### Face Mesh
```python
import aiocv
import cv2
img = cv2.imread("elon_musk.png")
# Make An Object
mesh = aiocv.FaceMesh()
# Use findFaceMesh() Method To Detect Face And Draw Mesh On Image/Video
mesh.findFaceMesh(img,draw=True)
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Params For findFaceMesh() Method :
```python
findFaceMesh(self,img=None,draw=True)
```
#### If You Are Not Getting Desired Results, Consider Changing detectionConfidence = 1 and trackConfidence = 1
#### Output :
![Face Mesh Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example2.png)
#### Contour (Shape) Detection
```python
import aiocv
import cv2
img = cv2.imread("shapes.png")
# Make An Object
shape = aiocv.ContourDetector(img)
# Use findContours() Method To Detect Shapes On Image/Video
shape.findContours(img,draw=True)
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Output :
![Contour Detection Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example5.png)
#### Car Detection
```python
import aiocv
import cv2
img = cv2.imread("car.png")
# Make An Object
car = aiocv.CarDetector(img)
# Use findCars() Method To Detect Cars On Image/Video
car.findCars()
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Params For findCars() Method :
```python
findCars(self,color=(255,0,0),thickness=2)
```
#### Output :
![Car Detection Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example9.png)
#### Number Plate Detection
```python
import aiocv
import cv2
img = cv2.imread("car.png")
# Make An Object
car = aiocv.NumberPlateDetector(img)
# Use findNumberPlate() Method To Detect Number Plate On Image/Video
car.findNumberPlate()
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Params For findNumberPlate() Method :
```python
findNumberPlate(self,color=(255,0,0),thickness=2)
```
#### Output :
![Number Plate Detection Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example6.png)
#### Smile Detection
```python
import aiocv
import cv2
img = cv2.imread("person.png")
# Make An Object
smile = aiocv.SmileDetector(img)
# Use findSmile() Method To Detect Smile On Image/Video
smile.findSmile()
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Params For findSmile() Method :
```python
findSmile(self,color=(255,0,0),thickness=2)
```
#### Output :
![Smile Detection Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example7.png)
#### Eyes Detection
```python
import aiocv
import cv2
img = cv2.imread("person.png")
# Make An Object
eyes = aiocv.EyesDetector(img)
# Use findEyes() Method To Detect Eyes On Image/Video
eyes.findEyes()
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Params For findEyes() Method :
```python
findEyes(self,color=(255,0,0),thickness=2)
```
#### Output :
![Eyes Detection Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example8.png)
#### Control Volume Using Gesture
```python
import aiocv
# Make An Object
gvc = aiocv.GestureVolumeControl()
# Use controlVolume() Method To Control Volume
gvc.controlVolume()
```
#### Params For controlVolume() Method :
```python
controlVolume(self,color=(255,0,0),thickness=2)
```
#### Params For GestureVolumeControl Class :
```python
gvc = aiocv.GestureVolumeControl(webcamIndex = 0)
# If You Want To Control From Other Camera, Set The webcamIndex Accordingly.
```
#### Output :
![Gesture Volume Control Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example10.png)
#### Read QR Code
```python
import aiocv
import cv2
img = cv2.imread("qr.png")
# Make An Object
qr = aiocv.QRCodeReader(img)
# Use findQRCode() Method To Detect QR Code On Image/Video
text=qr.findQRCode()
cv2.imshow("Image",img)
cv2.waitKey(0)
```
#### Params For findQRCode() Method :
```python
findQRCode(self,color=(255,0,0),thickness=3)
```
#### To Print The Extracted Text :
```python
print(text)
```
#### Output :
![QR Code Detected Image](https://raw.githubusercontent.com/0xN1nja/aiocv/master/examples/example11.png)
## Contributing
Pull Requests Are Welcome. For Major Changes, Please Open An Issue First To Discuss What You Would Like To Change.

Please Make Sure To Update Tests As Appropriate.

## License
[MIT](https://github.com/0xN1nja/aiocv/blob/master/LICENCE.txt)