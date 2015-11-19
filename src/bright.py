import numpy as np
import cv2

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)

    while(1):

        # Take each frame
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret,th1 = cv2.threshold(gray,170,255,cv2.THRESH_TOZERO)
        ret,th2 = cv2.threshold(th1,253,255,cv2.THRESH_BINARY)
        #first num is sidewards second num is up and down
        kernel = np.ones((5,5),np.uint8)
        #iterations is to make it smaler in general
        erosion = cv2.erode(th2,kernel,iterations = 8)
       
        cv2.imshow('frame',gray)
        cv2.imshow("thersh1",th1)
        cv2.imshow("thersh2",th2)
        cv2.imshow("thersh3",erosion)
        
       
        
        k = cv2.waitKey(2) & 0xFF
        if k == 27:
            break

cv2.destroyAllWindows()
