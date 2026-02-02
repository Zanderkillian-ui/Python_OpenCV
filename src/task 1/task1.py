#!/usr/bin/env python3

######### Task 1 ##########
# Create a class VideoPlayer. The class must have:
# 1. A constructor
# 2. One class method to display the frames
###########################
import numpy as np
import cv2 as cv
import os
import time

class VideoPlayer:

    def __init__(self):

        cdir = os.getcwd()
        self.cap = cv.VideoCapture(cdir+"/src/test_video.mp4")
        
        
    def frame_rate(self):
        if not self.cap.isOpened():
            print("Cannot open video file")
            rate = 0
            exit()
        
        start_time = time.time()
        frame_counter = 0

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Can't receive frame (video ended?). Exiting ...")
                break
            cv.imshow('frame', frame)
            frame_counter += 1
            if cv.waitKey(1) == ord('q'):
                break

        rate = frame_counter / (time.time() - start_time)
        print(f"Frame rate: {rate}")
        self.cap.release()
        cv.destroyAllWindows()
    
def main():

    video = VideoPlayer()
    video.frame_rate()

if __name__ == "__main__":
    main()
