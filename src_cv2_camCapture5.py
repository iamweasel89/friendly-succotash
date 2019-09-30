import numpy as np
import cv2
from matplotlib import pyplot as plt

params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0
params.maxThreshold = 25

# Set edge gradient
params.thresholdStep = 5

# Filter by Area.
params.filterByArea = True
params.minArea = 200
params.maxArea = 880

#Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):  # check !
    # capture frame-by-frame
    ret, frame = cap.read()

    if ret: # check ! (some webcam's need a "warmup")
        # our operation on frame come here
        #gray = frame
        th = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #th = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

        #th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                    #cv2.THRESH_BINARY,11,2)
        #th = cv2.GaussianBlur(th, (21, 21), 0)

        th = cv2.adaptiveThreshold(th,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    cv2.THRESH_BINARY,91,1)

        th = cv2.bitwise_not(th)



        #th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        #th = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

        # Detect blobs.
        keypoints = detector.detect(th)
        quan_keypoints = len(keypoints)
        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        th = cv2.drawKeypoints(th, keypoints, np.array([]), (0, 0, 255),
                                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.putText(th, str(quan_keypoints), (15, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 105, 210), 4)

        #cv2.putText(th, len(keypoints), (15, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 105, 210), 4)

        # Display the resulting frame
        cv2.imshow('frame', th)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done release the capture
cap.release()
cv2.destroyAllWindows()
