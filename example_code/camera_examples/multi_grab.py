#!/usr/bin/python3
import cv2
import time
camera_port = 0

camera = cv2.VideoCapture(camera_port)
start_time = time.time()
nframes = 1500
for ix in range(nframes):
    return_value, image = camera.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    #cv2.imwrite("opencv%03d.png" % ix, image)
end_time = time.time()
print('Time Elapsed: %f' % (end_time - start_time))
print('Realtime ratio: %f' % ( (nframes / 30)/(end_time - start_time)))

del(camera)  # so that others can use the camera as soon as possible
