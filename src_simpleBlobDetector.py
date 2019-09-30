# Standard imports
import cv2
import numpy as np

# Read image
im = cv2.imread("images\puzzles.jpg", cv2.IMREAD_COLOR)

width = 600
proportion = im.shape[0] / im.shape[1]
heigth = int(width * proportion)
print(heigth)
dim = (width, heigth)
im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0
params.maxThreshold = 255

# Set edge gradient
params.thresholdStep = 1

# Filter by Area.
params.filterByArea = True
params.minArea = 10

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
