#!/usr/bin/env python3

####### Import required modules ######
import cv2 as cv
from matplotlib import pyplot as plt
import os

### Importing custom module - ###
# Here, I imported the 'pixel_value' function from the 'return_values' module
# Modules are just another python files, which contain different functions or/and class methods definiition
from return_values import pixel_value
# The 'return_values' module doesn't have a class definition, only a single function. Hence,
# the syntax 'from <module_name> import <function_name>

# When a module has one or more class definitions, each with multiple class methods, 
# you can import the class, and then use the '.' operator to call the class methods. Or
# directly import one or more class methods.
# Example: 
# from matplotlib import pyplot
# This imports the pyplot class from the matplotlib module
# But ...
# from matplotlib import pyplot.subplot as subplot
# from matplotlib import pyplot.title as title
# from matplotlib import pyplot.xticks as xticks
# from matplotlib import pyplot.yticks as yticks
# These will import the subplot, title, xticks, yticks, class methods of class pyplot directly.

# Get the current working directory
# For this example to work, your current directory should be Python_OpenCV
cdir = os.getcwd()

# Read an image, and convert it into gray-scale
img = cv.imread(f'{cdir}/src/task2/Entry_Exit_Gate.png', cv.IMREAD_COLOR_RGB)
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Check if you can read the image or not
assert img is not None, "file could not be read, check with os.path.exists()"

######### Thresholding ##########
# Thresholding is a concept in computer vision, which basically refers to isolating
# target pixels out of all the pixels in an image. It is done using the color value
# of the pixels. 

# Every color is a combination of three base colors - Red, Green, Blue. And Each base
# values, range from 0-255. So, [0, 0 ,0] corresponds to Black, while [255, 255, 255]
# corresponds to white.

# Before thresholding, it is generally preferred to convert the image to gray scale,
# which basically reduces the images from a 3D array to 2D array. Now, instead of 
# three values, each pixel only has one value for color, in the range of 0-255.
# This reduces, computational load, and ease the process of thresholding.

# For every pixel, the same threshold value is applied. If the pixel value is 
# smaller than or equal to the threshold, it is set to 0, otherwise it is set to a 
# maximum value, which is genrally 255.

# OpenCv offers various thresholding methods, you can read it here - 
# https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
# Here I am using the simplest method cv.THRESH_BINARY

# There is no rule of thumb to pick thresholding value. You can use method of your choice.
# Here, I start with any random value. Then complete the code/logic around that.
# At the end, when the figure window pops-up, hover your mouse above area/region, on the
# gray-scaled image. And note the values at the top-right corner of the figure window.
# One of then is the pixel location, and the other is the pixel value. 

# In this example, I am extracting the red buoys. The red buoys, don't have a single shade
# of color red. Depending on the light falling on the buoy, some area have a lighter shade,
# while some darker. I picked, a value close of the lighter red color, as based on the 
# thresholding definition, the pixels with color values less than threshold will automatically 
# become zero.

# This is a tuning process. So, it is fine if it takes you multiple attempts to find the 
# right thresholding value

ret,mask = cv.threshold(gray_img,88,255,cv.THRESH_BINARY)

# A black-white image, in computer vision is generally called a mask. 
# And used to remove objects from the image. White pixels are kept while black pixels are 
# the one, which gets removed.
# The mask that I just created, has objects of my interest in black, while rest in white.
# So, I need to invert it.
mask_inv = cv.bitwise_not(mask)

# Now, Remove the backgroud from the foreground
masked_img = cv.bitwise_and(img,img,mask = mask_inv)

# Show the images in the figure
titles = ['Original Image','Grayscale', 'Mask', 'Extracted']
images = [img, gray_img, mask_inv, masked_img]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

    # Print the color of the pixel located at [43, 268]
    px_value = pixel_value(images[i], [43, 268])
    print(px_value)

plt.show()