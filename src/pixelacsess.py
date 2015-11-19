import numpy as np
import cv2

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)

    while(1):

        # Take each frame
        _, frame = cap.read()
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame2= cv2.line(frame2,(310,230),(330,250),(255,0,0),2)
        frame2= cv2.line(frame2,(330,230),(310,250),(255,0,0),2)
        pxRGB = frame[320,240]
        pxHSV = frame2[320,240]
        print "BGR " + str(pxRGB) + "   HSV " + str(pxHSV)
      
        cv2.imshow('HSV',frame2)
        cv2.imshow("BGR", frame)
        
        k = cv2.waitKey(100) & 0xFF
        if k == 27:
            break

cv2.destroyAllWindows()
        