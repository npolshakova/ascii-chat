import cv2
import time

capture = cv2.VideoCapture(0)
while(True):
    start = time.time()
    ret, frame = capture.read()
    end = time.time()
    print("time to read a frame : {} seconds".format(end - start))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
