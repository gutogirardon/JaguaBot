from jaguabot.libraries.image_search import region_grabber
import numpy as np


def find_pixel_color(color, end_bar_color, deviation, x1, y1, x2, y2, image=None):
    if image is None:
        image = region_grabber((x1, y1, x2, y2))
    im = np.array(image)
    rows = im.shape[0]
    cols = im.shape[1]
    for i in range(rows):
        for j in range(cols):
            pixel = im[i, j]
            if RGB_deviations(color, end_bar_color, pixel, deviation):
                match = (int(j+x1+1), int(i+y1))
                return match
    no_match = (-1, -1)
    return no_match

def RGB_deviations(color, end_bar_color, pixel, deviation):
    R = pixel[0:1]
    G = pixel[1:2]
    B = pixel[2:3]
    if color[0] - R >= -deviation and color[0] - R <= deviation:
        if color[1] - G >= -deviation and color[1] - G <= deviation:
            if color[2] - B >= -deviation and color[2] - B <= deviation:
                return True

    if R == end_bar_color[0]:
        if G == end_bar_color[1]:
            if B == end_bar_color[2]:
                # we are at full HP or mana
                return True
    return False