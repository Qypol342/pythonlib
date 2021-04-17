import cv2
import sys
from PIL import Image, ImageFilter


imagePath = 'images/c1.png'
def search_face(imagePath):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
    )

    #print("Found {0} Faces!".format(len(faces)))


    for (x, y, w, h) in faces:
        if w >=85 and h>=85:
            roi_color = image[y:y + h, x:x + w]
            roi_color = cv2.resize(roi_color, (85,85), interpolation = cv2.INTER_AREA)
            roi_color =cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('images/_faces.png', roi_color)
            im  = Image.fromarray(cv2.cvtColor(roi_color, cv2.COLOR_BGR2RGB))
            im = im.filter(ImageFilter.CONTOUR)
            im.save('images/C_faces.png')
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            


    status = cv2.imwrite('images/faces_detected.png', image)