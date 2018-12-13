import cv2
import numpy as np
from PIL import ImageGrab

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        
        return jpeg.tobytes()


class ScreenCamera(object):
    def __init__(self):
        self.bool = True

    def get_frame(self):
        img = ImageGrab.grab()
        img = np.array(img) 
        a, img = cv2.imencode('.jpg', img)
        return img.tobytes()


