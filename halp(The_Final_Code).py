import numpy as np
import cv2
import os
from PIL import Image
import imageClassifier

cap = cv2.VideoCapture(0)
# data = imageClassifier.ImageSorter()

stepX = 20
stepY = 15

image_db = []
for filename in os.listdir('cartoons'):
	pil_image = Image.open(os.path.join('cartoons', filename)).convert('RGB') 
	open_cv_image = np.array(pil_image) 
	# Convert RGB to BGR 
	open_cv_image = open_cv_image[:, :, ::-1].copy() 
	image_db.append(cv2.resize(open_cv_image, (stepX, stepY)))

# cv2.imshow('yolo', image_db[0])
# cv2.waitKey(0)
# print len(image_db)
# exit()

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	cv2.imshow("image", frame)
	cv2.waitKey(1)
	for x in xrange(0, frame.shape[1], stepX):
		for y in xrange(0, frame.shape[0], stepY):
			sub_img = frame[y:y+stepY, x:x+stepX]
			# print sub_img.shape
			if sub_img.shape[0] != stepY or sub_img.shape[1] != stepX:
				pass
			else:
				# sub_pxl = cv2.resize(sub_img, (1, 1))
				# rgb = sub_pxl[0,0]

				# img = imageClassifier.ImageSorter.getBestImage(data, rgb[0], rgb[1], rgb[2], data.images)
				# icon = cv2.resize(cv2.imread(img.name), (stepX, stepY))

				best_img = None
				min_dist = 10**3

				for im in image_db:
					diff = np.absolute(im - sub_img)
					m = np.mean(diff, dtype=np.float32)
					if m < min_dist:
						best_img = im
						min_dist = m
				#print min_dist

				frame[y:y+im.shape[0], x:x+im.shape[1]] = best_img
				cv2.imshow("image", frame)
				cv2.waitKey(1)

	cv2.imshow("image", frame)
	
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
