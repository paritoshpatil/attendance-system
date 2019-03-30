"""
ITF: Python code to take images from source/Dataset and use them to train an image recognizer
that can later be used to recognize faces of users and mark their attendance

Using: 
OpenCV2 for creating and training recognizer over dataset
Python Image Library (PIL) for converting images to openCV readable format
Numpy to create and manage image arrays

Training data is stored as TrainingData.yml file in source folder to be used later
"""

from PIL import Image
import numpy as np
import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()	#create recognizer as LBPHFaceRecognizer object from openCV library


def getImagesWithID(path):
	imagePaths = [os.path.join(path, f) for f in os.listdir(path)]	#store path of every image in dataset in imagePaths list
	faces = []	#create faces list
	ids = []	#create ids list

	for imagePath in imagePaths:	#loop thorough every image in Dataset
		facePil = Image.open(imagePath).convert('L')	#convert image to Python Image Library
		faceNp = np.array(facePil, 'uint8')		#convert PIL image to NumPy array using uint8 decoding

		currentID = int(os.path.split(imagePath)[-1].split(".")[1])	#get current id of user from file name
		print(currentID)
		faces.append(faceNp)	#append numpy array to faces list
		ids.append(currentID)	#append relative id to id list

		# cv2.imshow("train", faceNp)
		# cv2.waitKey(0)

	return np.array(ids), faces	#function returns faces and id list, id list is also converted to numpy array

dataPath = "Dataset"
ids, faces = getImagesWithID(dataPath)
recognizer.train(faces, ids)	#recognizer is trained with faces and id list from dataset
recognizer.save("trainingData.yml")	#save recognizer configuration as yml file
cv2.destroyAllWindows()
