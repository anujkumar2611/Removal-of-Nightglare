import cv2
import argparse
import numpy as np

image = cv2.imread("glare2.jpg") 
if image is None:
    print('Could not open or find the image: ')
    exit(0)

# Creating kernel
kernel = np.ones((3, 3), np.uint8)
# Using cv2.erode() method 
image_erode = cv2.erode(image, kernel, iterations=2)
filename = 'ErodeImage.jpg'
cv2.imwrite(filename, image_erode)



img_1 = image_erode
# for gamma in [0.6, 0.9, 1.2]:
gamma = 0.6
gamma_corrected = np.array(255*(img_1 / 255) ** gamma, dtype = 'uint8')
cv2.imwrite('gamma_'+str(gamma)+'.jpg', gamma_corrected)
img = gamma_corrected
image_border1 = cv2.copyMakeBorder(img, 25, 25, 10, 10, cv2.BORDER_CONSTANT, None, value = 0)

filename = 'BorderImage.jpg'
cv2.imwrite(filename,image_border1)