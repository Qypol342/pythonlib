import cv2
from findface import search_face
import threading

cap = cv2.VideoCapture(0)


def take(path):
	 # video capture source camera (Here webcam of laptop) 
	ret,frame = cap.read() # return a single frame in variable `frame`
	cv2.imwrite(path,frame)
	#cap.release()

path = 'images/raw.png'
for i in range(5):
	take(path)
	search_face(path)

cap.release()
