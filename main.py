# Importing Modules

import cv2
import numpy as np
import face_recognition as face
import os
from datetime import datetime


# Decalring Important Variables

path = 'Images'
images = []
userNames = []
UserList = os.listdir(path)



# This lists all the Users in the User List

for user in UserList:
    currentImg = cv2.imread(f'{path}/{user}')
    images.append(currentImg)
    userNames.append(os.path.splitext(user)[0])



# This converts the image in the Binary/Encoded Form

def findEncodings(images):
    encodeList = []
    for img in images:
       img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
       encode = face.face_encodings(img)[0]
       encodeList.append(encode)
    return encodeList



# This Function Marks Attendance in the Database according to the Recognition from the Encoded Form

def markAttendance(name):
    with open('Database/Attendance.csv','r+',) as csv:
        DataList = csv.readlines()
        nameList = []
        for line in DataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%I:%M %p')
            csv.writelines(f'\n{name}, {dtString}')



# Known Faces
KnownFaces = findEncodings(images)

# This open the Camera and Starts Live Video Capture
'''You can change the value of 0 to 1 if you have 2 cameras. You can chage it so
   you can have better quality Video.
'''
cam = cv2.VideoCapture(0)


while True:
    # Tells that *img* is the LiveCam Shoot
    success, img = cam.read()
    
    # Converts the Image in half so that it could Render Fast
    imgSmall = cv2.resize(img, (0,0), None, 0.5, 0.5)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)
    
    # Framerate of Image and their Encodings
    FacesCurrentFrame = face.face_locations(imgSmall)
    EncodesCurrentFrame = face.face_encodings(imgSmall, FacesCurrentFrame)
    
    # Organizes Faces and Manages Face Locations and their Matching Index
    for EncodedFace,FaceLocation in zip(EncodesCurrentFrame, FacesCurrentFrame):
        matches = face.compare_faces(KnownFaces, EncodedFace)
        faceDis = face.face_distance(KnownFaces, EncodedFace)
        matchIndex = np.argmin(faceDis)
        
        
        if matches[matchIndex]:
            name = userNames[matchIndex]
            
            # These nums are the Coordinates for the Locations on the Face
            y1,x2,y2,x1 = FaceLocation
            
            # You remeber earlier, we halfed the Image to Render Fast we bring it to Normal for Proper Coordinates Visible
            y1,x2,y2,x1 = y1*2,x2*2,y2*2,x1*2
            
            # Draws the Reactangle Around the Face according to Coordinates with their names
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,0),3)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            
            # As it identifies the Face it adds the name it to the Database *csv*
            markAttendance(name)

# Title and the Window where you can see your Camera's Input   
    cv2.imshow('Live Camera',img)
    cv2.waitKey(1)