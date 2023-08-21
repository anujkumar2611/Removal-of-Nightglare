import cv2
import numpy as np

# Load the image
img = cv2.imread('C:\Users\verma\OneDrive\Desktop\VS Code\3rd year project\final\img3.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to the image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 25)

# Dilate the thresholded image to fill gaps
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations=1)

# Invert the dilation to create a mask
mask = cv2.bitwise_not(dilation)

# Apply the mask to the original image
result = cv2.bitwise_and(img, img, mask=mask)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
