# image_utils.py -- Functions for capturing (and maybe correcting?) webcam images

import cv2

def capture_image(camera_port=0):
    ''' Captures an image with openCV from the camera
        on the specified port (Webcam appears to default to 0
    '''
    camera = cv2.VideoCapture(camera_port)
    ret, image = camera.read()
    cv2.imwrit
