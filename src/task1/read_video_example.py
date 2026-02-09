#!/usr/bin/env python3

# Import important python modules
import numpy as np
import cv2 as cv
import os

# Get the current working directory
# For this example to work, your current directory should be Python_OpenCV
cdir = os.getcwd()
# Uncomment this to print your current working directory in the terminal
#print(cdir)

# Use the VideoCapture class from the opencv (cv2) module to read the 
# video file
cap = cv.VideoCapture(cdir+"/src/test_video.mp4")

# Check if the video file is valid? Can we open it?
# We use the isOpened method/function defined within the VideoCapture class
# of OpenCV module
if not cap.isOpened():
    print("Cannot open video file")
    # We the video file is invalid, we exit the code
    # No need to process rest of the code
    exit()

# If video file is valid, we read the frames one by one and display it
while True:
    # Capture frame-by-frame
    # Using the read method of the VideoCapture class
    # This function returns two things, the frame and a boolean, flagging a frame 
    # has been read correctly
    ret, frame = cap.read()

    # We use that boolean to indicate user, if the video ended or 
    # of some unexpected behavior
    if not ret:
        print("Can't receive frame (video ended?). Exiting ...")
        # If we are no longer receiving frame, break out of the while loop
        break

    # If everything goes well, we have a frame
    # Display the resulting frame
    cv.imshow('frame', frame)

    # Press 'q' to exit the display early
    if cv.waitKey(0) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()