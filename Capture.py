import numpy as np 
import cv2
import os



#sample input images must be in folder samples with names p1, p2 ... pn.jpg

file_count = len(os.listdir("Samples"))	#count number of sample images in folder "samples"
faceCount = 0
for i in range(1, file_count):	#loop through all input images in folder "samples"
	img = cv2.imread("Samples/p"+str(i)+".jpg")	#read images in samples folder one by one
	face_casc = cv2.CascadeClassifier("haar_face.xml")
	# eye_casc = cv2.CascadeClassifier("haar_eye.xml")

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	#make grayscale copy of image as gray
	faces = face_casc.detectMultiScale(gray, 1.2, 5)	#detect faces on grayscale image and store in faces list


	#faces list stores faces as starting co-ordinate of each face along with its width and height i.e. face1 = (x,y) and width w height h
	for (x, y, w, h) in faces:	#loop through every face found in image
		cv2.imwrite("DatasetY/User."+str(faceCount)+".jpg", gray[y:y+h, x:x+w])	#cropped faces are saved in Dataset 
		cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),3)	#displays rectangles over faces in input images
		faceCount += 1	#facecounter

		# roi_gray = gray[y:y+h,x:x+w]
		# roi_color = img[y:y+h,x:x+w]
		# eyes = face_casc.detectMultiScale(roi_gray)
		# for (ex, ey, ew, eh) in eyes:
		# 	cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)

		cv2.imshow('img',img)
		
	print("Number of Faces: "+str(faceCount))
	cv2.waitKey(0)
	# cap.release()
	cv2.destroyAllWindows()