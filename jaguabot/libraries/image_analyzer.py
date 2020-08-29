"""
Source code adapted from: https://github.com/drov0/python-imagesearch
Credits to https://github.com/drov0
Documentation: https://brokencode.io/how-to-easily-image-search-with-python/
"""
from collections import defaultdict
import numpy as np
import cv2
import pyautogui

#constants
START_COORDS_DICT = defaultdict(list)
END_COORDS_DICT = defaultdict(list)
STATUS_BAR_DICT = defaultdict(list)

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

def image_search_area(image, x1, y1, x2, y2, precision=0.8, im=None):
    """
    Searchs for an image within an area

    :param image : path to the image file (see opencv imread for supported types)
    :param x1 : top left x value
    :param y1 : top left y value
    :param x2 : bottom right x value
    :param y2 : bottom right y value
    :param precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
    :param im : a PIL image, usefull if you intend to search the same unchanging region for several elements
    return the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
    """
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))
        # im.save('testarea.png') usefull for debugging purposes

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

def region_grabber(region):
    """
    Receive a region tuple = topx, topy, bottomx, bottomy
    The tuple contain the 4 coordinates of the region to capture
    Return a selected area
    :param region:
    :return:
    """
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1
    return pyautogui.screenshot(region=(x1, y1, width, height))

def append_global_dict(dict, key, values):
    for item in values:
        if item not in dict[key]:
            dict[key].append(item)