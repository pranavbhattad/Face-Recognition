import cv2
import numpy as np
import face_recognition as fr

imgPranav = fr.load_image_file('Images/shriya.jpg')
imgPranav = cv2.cvtColor(imgPranav,cv2.COLOR_BGR2RGB)
imgTest = fr.load_image_file('Images/ath.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = fr.face_locations(imgPranav)[0]
encodePranav = fr.face_encodings(imgPranav)[0]
cv2.rectangle(imgPranav,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,0,0),2)

faceLocTest = fr.face_locations(imgTest)[0]
encodeTest = fr.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(0,0,0),2)

results = fr.compare_faces([encodePranav],encodeTest)
dif = fr.face_distance([encodePranav], encodeTest)
print(results,dif)

cv2.imshow('Papa', imgPranav)
cv2.imshow('Papa Test', imgTest)
cv2.waitKey(0)