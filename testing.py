import numpy as np
import cv2

def getAverageRGB(src):
	rgb = [0,0,0]
	for y in range(src.shape[0]):
		for x in range(src.shape[1]):
			for i in range(0,3):
				rgb[i] += src[y][x][i]
	print src
	fin = [0,0,0]
	for i in range(0,3):
		fin[i] = rgb[i]/(src.shape[0]*src.shape[1])
	return fin

def pixelate(src):
	xres = 16
	yres = 12
	size = yres, xres, 3
	frame = np.zeros(size, dtype=np.uint8)
	pixWidth = src.shape[1]/xres
	pixHeight = src.shape[0]/yres
	for y in range(yres):
		for x in range(xres):
			print x,y
#			print getAverageRGB(src[y*pixHeight:(y+1)*pixHeight, x*pixWidth:(x+1)*pixWidth])
   			frame[y][x] = getAverageRGB(src[y*pixHeight:(y+1)*pixHeight, x*pixWidth:(x+1)*pixWidth])
   	return frame

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
#    kernel = np.ones((5,5),np.uint8)
    # Our operations on the frame come here
#    crop = cv2.dilate(frame, kernel, iterations = 1)
    print frame.shape
    pixels = pixelate(frame)
    print pixels
    size = pixels.shape[1]*10, pixels.shape[0]*10, 3
    frame = np.zeros(size, dtype=np.uint8)
    cv2.resize(pixels, frame, interpolation=cv2.INTER_LINEAR)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.waitKey(60000)

    break
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()