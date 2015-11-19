
__author__ = "thomas.duppenthaler"
__date__ = "$08.10.2015 15:05:50$"

import numpy as np
import cv2
color_tracker_window = "Color Tracker"

class ColorTracker:
    

    def __init__(self):
        self.cap = cv2.VideoCapture(0) 
        
 
    
    def colorTracking(color, hsv):
        
        if color =="red":
            lower_color = np.array([0,100,100])
            upper_color = np.array([4,255,255])
            
        elif color == "orange":
            lower_color = np.array([0,100,100])
            upper_color = np.array([4,255,255])
            
        elif color == "green":
            lower_color = np.array([0,100,100])
            upper_color = np.array([4,255,255])
        else:
            print "wrong color name"
            
    # Threshold the HSV image to get only blue colors
            
        mask = cv2.inRange(hsv, lower_color, upper_color)
            
        kernelClosing = np.ones((8,8),np.uint8)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelClosing)
    # erosion
        kernelErosion = np.ones((1,1),np.uint8)
        
        erosions = cv2.erode(closing,kernelErosion,iterations = 7)
            
        res = cv2.bitwise_and(frame,frame, mask= erosions)
          
            
    # surch contours
        im2, contours0, hierarchy = cv2.findContours(erosions,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
           
            
        contours = [cv2.approxPolyDP(cnt, 60, True) for cnt in contours0]
            
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
            
        cnt = contours[0]
            
            
        x,y,w,h = cv2.boundingRect(cnt)
            
        cv2.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)
            
            
        cv2.drawContours(res, contours, -1, (255,255,255), 3)  
     
        return res
            
            
            
    
           
     
        
        
    def run(self):
        while(1):

          # Take each frame
            _, frame = self.cap.read()

    # Convert BGR to HSV
            hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
    # Draw cross
            hsv= cv2.line(hsv,(310,230),(330,250),(255,0,0),2)
            hsv= cv2.line(hsv,(330,230),(310,250),(255,0,0),2)
    #get HSV value from the middle of the cross
            pxHSV = hsv[320,240]
            print "HSV " + str(pxHSV)
    # define range of blue color in HSV
    
        
            lower_red = np.array([0,100,100])
            upper_red = np.array([4,255,255])

        # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_red, upper_red)
           

        # Bitwise-AND mask and original image
            
        # closing
            kernel1 = np.ones((8,8),np.uint8)
            closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel1)
        # erosion
            kernel2 = np.ones((1,1),np.uint8)
            erosions2 = cv2.erode(closing,kernel2,iterations = 7)
            erosions = cv2.erode(closing,kernel2,iterations = 7)
            
            res = cv2.bitwise_and(frame,frame, mask= erosions)
          
            
        # surch contours
            im2, contours0, hierarchy = cv2.findContours(erosions,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
           
            
            contours = [cv2.approxPolyDP(cnt, 60, True) for cnt in contours0]
            
            contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
            
            cnt1 = contours[0]
            
            
            x,y,w,h = cv2.boundingRect(cnt1)
            
            cv2.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)
            
            
            cv2.drawContours(res, contours, -1, (255,255,255), 3)
            #print " "
            #print "x"+str(x) +"  y"+ str(y)+" | w"+str(w) +"  h"+ str(h)
            #print " "
            
           
           
            
         
            
            
            
            
            
            
            res3 = cv2.add(res,res2)
           
           
           
           
            
            cv2.imshow('gray',mask)
            cv2.imshow('hsv',hsv)
            cv2.imshow('res2',mask2)
            cv2.imshow('res',res3)
            cv2.imshow('closeing',closing)
            cv2.imshow('erosion',erosions2)
           
           
            k = cv2.waitKey(250) & 0xFF
            if k == 27:
                break
if __name__ == "__main__":
    color_tracker = ColorTracker()
    color_tracker.run()
   