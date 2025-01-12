import numpy as np
import cv2

def get_limit(color):
    c = np.uint8([[color]])  # here insert the BRG values which you want to convert into HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 160, 160
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    return lowerLimit, upperLimit


