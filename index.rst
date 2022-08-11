# AIOCV

aiocv Is A Python Library Used To Track Hands, Track Pose, Detect Face, Detect Contours (Shapes), Detect Cars, Detect Number Plate, Detect Smile, Detect Eyes, Control Volume Using Gesture And Create Face Mesh On Image/Video.

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
![Hand Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example4.png?raw=true)
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
![Pose Track Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example3.png?raw=true)
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
![Face Detection Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example1.png?raw=true)
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
![Face Mesh Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example2.png?raw=true)
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
![Contour Detection Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example5.png?raw=true)
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
![Car Detection Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example9.png?raw=true)
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
![Number Plate Detection Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example6.png?raw=true)
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
![Smile Detection Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example7.png?raw=true)
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
![Eyes Detection Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example8.png?raw=true)
#### Eyes Detection
```python
import aiocv
gvc=aiocv.GestureVolumeControl()
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
![Gesture Volume Control Image](https://github.com/N1nja0p/aiocv/blob/main/examples/example10.png?raw=true)
## Contributing
Pull Requests Are Welcome. For Major Changes, Please Open An Issue First To Discuss What You Would Like To Change.

Please Make Sure To Update Tests As Appropriate.

## License
[MIT](https://github.com/N1nja0p/aiocv/blob/main/LICENCE.txt)
