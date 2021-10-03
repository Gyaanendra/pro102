# security system
import dropbox
import time
import random
import cv2

start_time = time.time()


def capture():
    number = random.randint(1, 100)
    # to init cv2
    captured_img = cv2.VideoCapture(0)
    result = True
    while(result):
        # read the frames when cam is active
        ret, frame = captured_img.read()
        imgname = "image"+str(number)+".png"
        # to save the img
        cv2.imwrite(imgname, frame)
        start_time = time.time()
        result = False
    # to  stop the CAM
    captured_img.release()

    # to close all windows
    cv2.destroyAllWindows()


def upload(imgname):
    access_token = "fZqyEO7JXGEAAAAAAAAAAXPklSJJWCQbWjvZoPVShP1vtpn66dIoOk3_WxMiFx1D"
    file = imgname
    filefrom = file
    file_to = "/pro102/"+file
    # file.upload(filefrom, file_to)
    dbx = dropbox.Dropbox(access_token)
    with open(filefrom, "rb") as f:
        dbx.files_upload(f.read(), file_to,
                         mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while True:
        if ((time.time()-start_time) >= 5):
            n = capture()
            upload(n)


main()
