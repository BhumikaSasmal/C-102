import cv2
import dropbox
import time
import random
startTime=time.time()
def takeSnapShot():
    number = random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=videoCaptureObject.read()
        imgName= "image"+str(number)+".jpg"
        cv2.imwrite(imgName,frame)
        startTime = time.time()
        result = False
    return imgName 
    print("Snapshot has been taken.")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imgName):
    access_token = "sl.BFemxorP0m70ssx8C9ZowNb_JcSbVAcyemHKf4XQJUWV86JzKpgY_FkNdSYCfhUpzcsFNWqAEvVLOVdYAjOfumHzhr5GUI10-rh5iysmONgejwM5jGHrWum62kyxd7lZbk6egVZvDbWv"
    file_from = imgName
    file_to = "/imageFolder/"+imgName
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded.")

def main():
    while(True):
        if((time.time()- startTime)>= 5):
            name = takeSnapShot()
            uploadFile(name)
main()