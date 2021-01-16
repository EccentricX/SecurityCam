#Motion detection (big objects only)
import cv2
import winsound
cam= cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1 = cam.read()
    ret,frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)
    grey = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY) #converting into greyscale
    blur = cv2.GaussianBlur(grey,(5,5),0) #blur to evenup the surfaces and reduce noise
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY) #sharpening blur image
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1,contours,-1,(0,255,0),5)
    for c in contours:
        if cv2.contourArea(c) < 3000: #excluding objects with area < 3000 (3000 pixles i suppose.)
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.Beep(500,200)
    if cv2.waitKey(1)==ord('q'):
        break
    cv2.imshow('My Cam',frame1)
 