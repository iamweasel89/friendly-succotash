import cv2
from datetime import datetime

#stream = cv2.VideoCapture('http://10.10.1.234/snapshot.cgi?user=admin&pwd=')

# Use the next line if your camera has a username and password
# stream = cv2.VideoCapture('protocol://username:password@IP:port/1')
#now = datetime.now()
for x in range(1000):
    stream = cv2.VideoCapture('http://10.10.1.234/snapshot.cgi?user=admin&pwd=')
    r, f = stream.read()
    #p = R'images\'
    #p = str(x)
    #r'.jpg'
    #p = r'images\face-' + str(x) + '.jpg'
    #p = r'images\2019_' + datetime.now().strftime("%X") + str(x) + '.jpg'
    p = r'images\2019_' + str(x) + '.jpg'
    #p = r'images\' + r'face-' + str(x) + r'.jpg'
    #p = "face-" + str(x) + ".jpg"
    cv2.imwrite(p, f)
    #cv2.imshow('IP Camera stream',f)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
    print(p)
#cv2.destroyAllWindows()
