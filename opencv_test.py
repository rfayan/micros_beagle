from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    waitKey(1)
    destroyWindow("cam-test")
    imwrite("/home/alarm/simplecv2/foto.jpg",img) #save image

cam.release()
destroyAllWindows()

