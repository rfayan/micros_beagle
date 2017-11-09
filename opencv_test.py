from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    imwrite("/home/alarm/micros_beagle/shot.jpg",img) #save image

cam.release()
destroyAllWindows()

