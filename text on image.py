import cv2
import pytesseract
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('image w text.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#print(pytesseract.image_to_string(img))
#detection of characters
hImg, wImg, channels = img.shape
boxes= pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:

        b = b.split()
        print(b)
        if len(b)==12:
            x,y,w,h = int(b[6]), int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(255,255,255),2)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)

cv2.imshow('result',img)
cv2.waitKey(0)

#(pytesseract.image_to_string(img))
