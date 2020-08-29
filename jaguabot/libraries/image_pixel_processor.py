import numpy as np

from jaguabot.libraries.image_analyzer import region_grabber


def find_pixel_color(color, end_bar_color, deviation, x1, y1, x2, y2, image=None):
    """
    Find pixel color based in rgb values

    :param color:
    :param end_bar_color:
    :param deviation:
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param image:
    :return:
    """
    if image is None:
        image = region_grabber((x1, y1, x2, y2))
    im = np.array(image)
    rows = im.shape[0]
    cols = im.shape[1]
    for i in range(rows):
        for j in range(cols):
            pixel = im[i, j]
            if rgb_deviations(color, end_bar_color, pixel, deviation):
                match = (int(j+x1+1), int(i+y1))
                return match
    no_match = (-1, -1)
    return no_match

def rgb_deviations(color, end_bar_color, pixel, deviation):
    """

    :param color:
    :param end_bar_color:
    :param pixel:
    :param deviation:
    :return:
    """
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
                return True
    return False

def pixels_to_percent(start, end, current):
    """
    Convert pixel's to percentage

    :param start:
    :param end:
    :param current:
    :return:
    """
    total = end - start
    to_pc = total / 100
    current_pc = (current - start) / to_pc
    return current_pc
