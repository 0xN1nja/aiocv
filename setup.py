from setuptools import setup, find_packages
import os
VERSION = '0.0.35'
DESCRIPTION = 'aiocv Is A Python Library Used To Track Hands, Track Pose, Detect Face, Detect Contours (Shapes), Detect Cars, Detect Number Plate, Detect Smile, Detect Eyes, Control Volume Using Gesture, Read QR Codes And Create Face Mesh On Image/Video.'
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="aiocv",
    version=VERSION,
    author="Abhimanyu Sharma",
    author_email="speedcuberabhi@gmail.com",
    description=DESCRIPTION,
    packages=[".","haarcascades","aiocv"],
    package_data={'haarcascades':['*']},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['opencv-python', "mediapipe","msvc-runtime","pycaw","comtypes","qrcode","numpy"],
    keywords=['python',"machine-learning","mediapipe","deep-learning","tensorflow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)