import cv2
import os

def getframe(path , ms):
    cap = cv2.VideoCapture(path) #r"C:\Users\Admin\Downloads\segmentation.mp4"

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error opening video stream or file")
        return

    cap.set(cv2.CAP_PROP_POS_MSEC, ms)
    ret, frame = cap.read()
    cap.release()
    if ret:
        cv2.imwrite('foo'+str(ms)+'.png',frame)
        cwd = os.getcwd() + '/foo'+str(ms)+'.png'
        return cwd
    else:
        return

