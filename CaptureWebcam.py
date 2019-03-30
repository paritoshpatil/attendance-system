"""
ITF: Python code to capture Facial Data Samples from a user extracted from a live webcam feed

Using:
OpenCV2 for accessing and displaying webcam feed
Haar Cascades used for detecting faces from webcam feed

Faces are cropped and written to source/Dataset folder
"""

import numpy as np
import cv2 		#importing opencv2 library for image processing functions

#OBJECT DECLARATION
faceCasc = cv2.CascadeClassifier("haar_face.xml")	#loading haar cascade for face detection
cam = cv2.VideoCapture(0)		#cam object for accessing webcam feed
uid = int(input("Enter User ID ..."))	#accepting the user id from command line input
imgNumber = int(0)	#image counter

#MAIN CODE
while True:		#infinite loop for showing webcam feed
	ret, img = cam.read()	#reading frame from webcam feed
	img = cv2.flip(img, 1)	#flipping frame over a vertical axis to correct mirror effect
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	#converting frame to grayscale image
	faces = faceCasc.detectMultiScale(gray, 1.3, 5)	#detecting face(s) from feed using haar cascade and storing it in faces list

	#faces is a list that contains the starting co-ordinates and width and height of every face found in the frame
	for(x,y,w,h) in faces:	#looping through every face found in the frame

		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)	#drawing a rectangle around the faces
		cv2.imshow('Webcam Feed', img)	#displaying the frame in a new window 'webcam feed'

		if imgNumber == 0:	time.sleep(7)	#adding delay for the initial startup of the webcam feed

		imgNumber += 1
		cv2.imwrite("Dataset/User."+str(uid)+"."+str(imgNumber)+".jpg", gray[y:y+h, x:x+w])	#writing the cropped face image to Dataset Folder
		#naming scheme for dataset: User.<userID>.<userImageNumber>.jpg 

	if cv2.waitKey(100) & 0xFF == ord('q'):	break	#code to cut off camera feed when esc key is pressed
	# if cv2.waitKey(1) == 27:break
	elif(imgNumber > 30):	break	#also cut off webacm feed after 30 images of the faces are captured

cam.release()	#release webcam to os
cv2.destroyAllWindows()	#destroy all open windows
