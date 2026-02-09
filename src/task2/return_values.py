# Unlike C++, in python you can return values from every function or class methods.
# To return a value use the 'return' keyword with the value or variable that stores the value.
# Example:

import os
import cv2 as cv

# Path to directory
cdir = os.getcwd()

# Get the color value of the pixel which is at x-y location
def pixel_value(img, location):
    x_location = location[0]
    y_location = location[1]
    px_value = img[y_location,x_location] # [rows, column]

    return px_value

######### Uncomment this, if want to see the implementation ###########
# def main():
#     # Read an image, and convert it into gray-scale
#     img = cv.imread(f'{cdir}/src/task2/Entry_Exit_Gate.png', cv.IMREAD_GRAYSCALE)
#     # Check how many pixels we have in x and y direction
#     col, height = img.shape
#     print(f"Image size: {col} x {height}")

#     # Call the pixel_value function with the required arguments
#     # Make sure the x-y location for which you are inquiring for pixel value,
#     # doesn't fall out of the range of image size.
#     color_value = pixel_value(img, [150,150])

#     print(f"Pixel value: {color_value}")

# main()