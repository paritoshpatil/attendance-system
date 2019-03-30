"""
ITF: Python code to initialize a recognizer with Training Data from Trainer code and recognizing the user
face in a webcam feed

Using:
OpenCV2 for creating recognizer object and displaying webcam feed
Haar Cascade for detecting faces
"""

import numpy as np
import cv2


#OBJECT DECLARATION
cam = cv2.VideoCapture(0)	#object to access webcam feed	
face_casc = cv2.CascadeClassifier("haar_face.xml")	#loading haar cascade for face detection
currId = 0	#variable to store ID of current face

recog = cv2.face.LBPHFaceRecognizer_create()	#creating recognizer object 
recog.read("trainingData.yml")	#initialize recognizer with saved data

#MAIN CODE
while True:
	ret, img = cam.read()	#read frame from webcam
	img = cv2.flip(img, 1)	#flip webcam frame to correct mirror effect	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	#converting frame to grayscale
	faces = face_casc.detectMultiScale(gray, 1.3, 5)	#using haar cascade to detect faces

	for (x, y, w, h) in faces:	#for every face in frame, do- 

		cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),3)	#drawing rectangle around detected face

		currId, config = recog.predict(gray[y:y+h, x:x+h])	#predict the userID of the detected face

		cv2.putText(img,str(currId),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,255)	#displaying userID above detected face

		cv2.imshow('img',img)	#displaying frame

	if cv2.waitKey(1) == 27:	break

cam.release()
cv2.destroyAllWindows()
