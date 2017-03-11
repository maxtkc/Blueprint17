import numpy as np
import cv2
from PIL import Image
import imageClassifier

cap = cv2.VideoCapture(0)
data = imageClassifier.ImageSorter()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    newx,newy = frame.shape[1]/40,frame.shape[0]/40 #new size (w,h)
    newimage = cv2.resize(frame,(newx,newy))
    finalimage = np.zeros((newimage.shape[1]*40, newimage.shape[0]*30, 3), np.uint8)
    print finalimage.shape, newimage.shape
    for x in range(newimage.shape[1]):
    	for y in range(newimage.shape[0]):
    		img = imageClassifier.ImageSorter.getBestImage(data, newimage[x][y][0], newimage[x][y][1], newimage[x][y][2], data.images)
    		icon = cv2.imread(img.name)
    		finalimage[y*icon.shape[0]:(y+1)*icon.shape[0], x*icon.shape[1]:(x+1)*icon.shape[1]] = icon
    		print "x: ", x, "y: ", y
    cv2.imshow("original image", frame)
    cv2.imshow("resize image", newimage)
    cv2.imshow("finalimage", finalimage)
    # Display the resulting frame
    cv2.waitKey(10000)
    break
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# overlay = ...
# background= ...

# background[3:100,4:700] = overlay