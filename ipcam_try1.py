import cv2

#stream = cv2.VideoCapture('http://10.10.1.234/snapshot.cgi?user=admin&pwd=')

# Use the next line if your camera has a username and password
# stream = cv2.VideoCapture('protocol://username:password@IP:port/1')

while True:
    stream = cv2.VideoCapture('http://10.10.1.234/snapshot.cgi?user=admin&pwd=')
    r, f = stream.read()
    cv2.imshow('IP Camera stream',f)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
