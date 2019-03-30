# attendance-system
Automated Attendance System using Facial Recognition and Machine Learning

The objective of this system is to automate the process of marking attendance of students in an educational institute using facial recognition. This is done by clicking a photo of the class and feeding it into a faceial recognizer trained over the students faces, then detecting which students are present in the photo and marking their attendance in a student database.

First, a dataset of the face images of all the students is created using a webcam feed from a registration laptop.
This is done using openCV for the image processing features and haar cascades to detect faces from the feed

Secondly, a recognizer is trained over this dataset. The userID of the particular user in the image is taken from the file name using the unique naming scheme described in the code itself. The training data is stored as a .yml file for later use. 

Thirdly, a recognizer is created and loaded with the training data we previously saved. Now, the input image of the class is taken and the recognizer is used to recognize the faces of the students and mark their attendance into the database using sqlite connectivity in Python. 

***This code is a work in progress and so the database functionality is still unimplemented
