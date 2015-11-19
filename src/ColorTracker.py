#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "thomas.duppenthaler"
__date__ = "$08.10.2015 15:05:50$"

import numpy as np
import cv2
color_tracker_window = "Color Tracker"

class ColorTracker:
    

    def __init__(self):
        self.cap = cv2.VideoCapture(1) 
        
 
    
    def colorTracking(self, color, frame, hsv):
        
        if color =="red":
            lower_color = np.array([173,150,120])
            upper_color = np.array([180,255,255])
            
            conutrColor = (0,0,255)
            
        elif color == "orange":
            lower_color = np.array([5,100,100])
            upper_color = np.array([8,255,255])
            
            conutrColor = (0,145,255)
            
        elif color == "green":
            lower_color = np.array([70,100,30])
            upper_color = np.array([80,255,255])
            
            conutrColor = (0,185,0)
            
        else:
            print "wrong color name"
            
     # Threshold the HSV image to get only blue colors
       
            
        mask = cv2.inRange(hsv, lower_color, upper_color)
            
        kernelClosing = np.ones((16,16),np.uint8)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelClosing)
     # erosion
        kernelErosion = np.ones((1,1),np.uint8)
        
        erosions = cv2.erode(closing,kernelErosion,iterations = 5)
        
          
        res = cv2.bitwise_and(frame,frame, mask= erosions)
        
        #just help
        res2 = cv2.bitwise_and(frame,frame, mask= erosions)
        
            
     #  surch contours
        im2, contours0, hierarchy = cv2.findContours(erosions,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
           
            
        contours = [cv2.approxPolyDP(cnt, 40, True) for cnt in contours0]
            
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
        x = 0
        y=0
        w=0
        h=0
        
        if len(contours) > 0:
            cnt = contours[0]
            x,y,w,h = cv2.boundingRect(cnt)
            
            if w*h >= 1000:
            
                cv2.rectangle(res,(x,y),(x+w,y+h),conutrColor,2)
                print color
            
            
        cv2.drawContours(res2, contours, -1, (255,0,255), 2)  
     
        return res, res2, x,y,w,h
            
            
            
    
           
     
        
        
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
    
            
            orange = self.colorTracking("orange",frame,hsv)
            red = self.colorTracking("red",frame,hsv)
            green = self.colorTracking("green",frame,hsv)
            
            res2 = cv2.add(red[0],orange[0])
            res = cv2.add(res2, green[0])
            
            cv2.rectangle(res,(red[2],red[3]),(green[2]+green[4],green[3]+green[5]),(255,0,255),3)
           
           
           
            cv2.imshow('hsv',hsv)
            cv2.imshow('red',red[1])
            cv2.imshow('orange',orange[1])
            cv2.imshow('green',green[1])
            cv2.imshow('res',res)
            
           
           
            k = cv2.waitKey(25) & 0xFF
            if k == 27:
                break
if __name__ == "__main__":
    color_tracker = ColorTracker()
    color_tracker.run()
   

    


