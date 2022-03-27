import cv2 as cv
import os
import sys

# Windows uses DirectShow for video capture
camera = cv.VideoCapture(0, cv.CAP_DSHOW) if sys.platform.startswith("win") else cv.VideoCapture(0)

if not camera.isOpened():
    print("the camera is not opened")
    exit()
Labels=['G-man', 'G-man-Badge', 'Bootlegger', 'Rifle']
for label in Labels:
    if not os.path.exists(label):
        os.mkdir(label)
for folder in Labels:
    #using count variable to name the images in the dataset.
    count = 0
    #Taking input to start the capturing
    print("Press 's' to start data collection for "+folder)
    userinput = input()
    if userinput != 's':
        print("Wrong Input..........")
        exit()
    #clicking 200 images per label, you could change as you want.
    while count<200:
        #read returns two values one is the exit code and other is the frame
        status, frame = camera.read()
        #check if we get the frame or not
        if not status:
            print("Frame is not been captured..Exiting...")
            break
        #convert the image into colorformat for fast caculation
        color = cv.cvtColor(frame, cv.COLOR_BGR2RGB) #cv2.cvtcolor(img cv2.color_bgr2rgb)
        #display window with colorimage
        cv.imshow("Video Window",color)
        #resizing the image to store it
        color= cv.resize(color, (500,500)) #this changes size of the photo
        #Store the image to specific label folder
        cv.imwrite(f"./{folder}"+'/img'+str(count)+'.png',color)
        count=count+1
        #to quite the display window press 'q'
        if cv.waitKey(1) == ord('q'):
            break
# When everything done, release the capture
camera.release()
cv.destroyAllWindows()