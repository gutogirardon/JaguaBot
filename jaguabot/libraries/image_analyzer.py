"""
Source code adapted from: https://github.com/drov0/python-imagesearch
Credits to https://github.com/drov0
Documentation: https://brokencode.io/how-to-easily-image-search-with-python/
"""
import cv2
import numpy as np
import pyautogui

def image_search(image, precision=0.8):
    """
    Search for elements on the screen based on an image

    :param image: path to image
    :param precision: default = 0.8
    :return: the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
    """
    img = pyautogui.screenshot()
    img_rgb = np.array(img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    #max_val = LocatedPrecision and max_loc = Position
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc