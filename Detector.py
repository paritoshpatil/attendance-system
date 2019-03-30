import numpy as np
import cv2


faceCount = 0
img = cv2.imread("faces1.jpg")	#read images in samples folder one by one
face_casc = cv2.CascadeClassifier("haar_face.xml")
# eye_casc = cv2.CascadeClassifier("haar_eye.xml")

currId = 0
recog = cv2.face.LBPHFaceRecognizer_create()	
recog.read("trainingData.yml")	#initialize recognizer with saved data

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_casc.detectMultiScale(gray, 1.3, 5)

#font1 = cv2.InitFont(cv2.CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1, 0, 3)

for (x, y, w, h) in faces:
	#cv2.imwrite("Dataset/User."+str(faceCount)+".jpg", gray[y:y+h, x:x+w])
	cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),3)

	currId, config = recog.predict(gray[y:y+h, x:x+h])

	cv2.putText(img,str(currId),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,255)
	faceCount += 1

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
