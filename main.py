import cv2
import numpy as np
import face_recognition
import os

path = 'Images'
images = []
classNames = []
myList = os.listdir(path)
print (myList)

for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
       img = cv2.cvtColor() 
        