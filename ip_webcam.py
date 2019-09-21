import cv2

cap=cv2.VideoCapture('https://192.168.43.1:8080/video')
print("we got the device")
while(True):
    rlt,frame=cap.read() #reads 2 data- true/false value and image frame 
    cv2.imshow('frame' , frame)  #shows the detected image frame
    cv2.waitKey(1)  #so that we continuously get images to get a video
