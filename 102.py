import cv2 
def takeSnapShot():
    videoCaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("image1.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
takeSnapShot()
