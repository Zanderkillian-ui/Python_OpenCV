#!/usr/bin/env python3

######### Task 2 ##########
# 1. Create a module that has following methods - convertToGray, threshold, invert_mask
# 2. Import this custom module to use these defined class methods in this file.
# 3. Use Object-Oriented Programming to read frames from the 'test_video.mp4', 
#    extract the red and green becon placed on the dock.
# 
# Useful Suggestion:
# 1. For initial developement use the 'dock.png'
# 2. Use 0 instaed of 1 in the 'waitKey' function, to play the video frame by frame. Press any key
#    to roll through frames. *Note - Some frames might look frozen, but continue rolling. Its just how I recorded the video.
###########################
import cv2 as cv
from matplotlib import pyplot as plt
import os
from return_values import pixel_value

class BeconFinder:

    def __init__(self):
        # cdir = os.path.dirname(os.path.abspath(__file__))   
        # self.img = cv.imread(os.path.join(cdir, 'dock.png'))
        # assert self.img is not None, "file could not be read, check path"
        self.img = None

    def convertToGray(self):
        self.gray_img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)

    def threshold(self):
        ret,self.mask = cv.threshold(self.gray_img,88,255,cv.THRESH_BINARY)

    def invert_mask(self):
        self.mask_inv = cv.bitwise_not(self.mask)
        self.masked_img = cv.bitwise_and(self.img,self.img,mask = self.mask_inv)

    def getgray_img(self):
        return self.gray_img

    def getmaskandmasked(self):
        return self.mask_inv, self.masked_img
    
    def process_frame(self, frame):
        self.img = frame

        self.convertToGray()
        self.threshold()
        self.invert_mask()

        return self.getgray_img(), *self.getmaskandmasked()

    def detect_beacons(self, frame):
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # RED
        lower_red1 = (0, 120, 70)
        upper_red1 = (10, 255, 255)
        lower_red2 = (170, 120, 70)
        upper_red2 = (180, 255, 255)

        mask_red1 = cv.inRange(hsv, lower_red1, upper_red1)
        mask_red2 = cv.inRange(hsv, lower_red2, upper_red2)
        red_mask = cv.bitwise_or(mask_red1, mask_red2)

        # GREEN
        lower_green = (40, 70, 70)
        upper_green = (80, 255, 255)
        green_mask = cv.inRange(hsv, lower_green, upper_green)

        # Get all centers
        red_centers = self.get_all_centers(red_mask)
        green_centers = self.get_all_centers(green_mask)

        return red_centers, green_centers, red_mask, green_mask
    
    def get_center(self, mask):
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        if contours:
            largest = max(contours, key=cv.contourArea)
            M = cv.moments(largest)

            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                return (cx, cy)
    
    def get_all_centers(self, mask):
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        centers = []

        for cnt in contours:
            area = cv.contourArea(cnt)

         # Ignore tiny noise
            if area > 50:
                M = cv.moments(cnt)
                if M["m00"] != 0:
                  cx = int(M["m10"] / M["m00"])
                  cy = int(M["m01"] / M["m00"])
                  centers.append((cx, cy))

        return centers

def main():

    # img = BeconFinder()
    # img.convertToGray()
    # img.threshold()
    # img.invert_mask()
    # gray_img = img.getgray_img()
    # mask_inv, masked_img = img.getmaskandmasked()

    # titles = ['Original Image','Grayscale', 'Mask', 'Extracted']
    # images = [img.img, gray_img, mask_inv, masked_img]

    # for i in range(4):
    #     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    #     plt.title(titles[i])
    #     plt.xticks([]),plt.yticks([])

    #     # Print the color of the pixel located at [43, 268]
    #     px_value = pixel_value(images[i], [43, 268])
    #     print(px_value)

    # plt.show()
    cdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    video_path = os.path.join(cdir, 'test_video.mp4')

    cap = cv.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video")
        print("Tried path:", video_path)
        return

    processor = BeconFinder()
    frame_count = 0

    print("Press any key to step frames, 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("End of video")
            break

        frame_count += 1
        print(f"\nFrame {frame_count}")

        gray_img, mask_inv, masked_img = processor.process_frame(frame)
        # Find Beacons and Circles them
        red_centers, green_centers, red_mask, green_mask = processor.detect_beacons(frame)

        # Draw red beacons
        for (x, y) in red_centers:
         cv.circle(frame, (x, y), 6, (0, 0, 255), -1)
         cv.putText(frame, f"R({x},{y})", (x+5, y-5),
                     cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

        # Draw green beacons
        for (x, y) in green_centers:
             cv.circle(frame, (x, y), 6, (0, 255, 0), -1)
             cv.putText(frame, f"G({x},{y})", (x+5, y-5),
               cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

        print("Red beacons:", red_centers)
        print("Green beacons:", green_centers)

        # Display
        cv.imshow("Original", frame)
        # cv.imshow("Grayscale", gray_img)
        # cv.imshow("Mask", mask_inv)
        # cv.imshow("Extracted", masked_img)

        # Pixel value
        try:
            px_value = pixel_value(frame, [43, 268])
            print("Pixel value at (43,268):", px_value)
        except Exception as e:
            print("Pixel error:", e)

        key = cv.waitKey(0)

        if key == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()



if __name__ == "__main__":
    main()





