import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


# read in the image
image = mpimg.imread('test_lines\solidWhiteCurve.jpg')

# convert to greyscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# set kernel size and gaussian smooth/blur
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

# define parameters for Canny and call it
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# create a masked image
mask = np.zeros_like(edges)
ignore_mask_color = 255

# define the four sided polygon to mask
imshape = image.shape
vertices = np.array([[(0,imshape[0]),((5/11)*imshape[1], (6/11) * imshape[0]), ((6/11) * imshape[1], (6/11) * imshape[0]), (imshape[1],imshape[0])]], dtype=np.int32)
cv2.fillPoly(mask, vertices, ignore_mask_color)
masked_edges = cv2.bitwise_and(edges, mask)

# define the Hough transform parameters
rho = 1
theta = np.pi/180
threshold = 7
min_line_length = 20
max_line_gap = 3

# copy the image as a blank to draw on
line_image = np.copy(image) * 0

# Hough transform edge detected image, "lines" is an array containing endpoints
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

# draw lines on a blank image
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

# create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges)) 

# draw the lines on the edge image
lines_edges = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
plt.imshow(lines_edges)
