"""
Get Coordinates from user screen
"""
import os
import pyautogui
import cv2

from jaguabot.libraries.image_pixel_processor import find_pixel_color, pixels_to_percent
from jaguabot.libraries.image_analyzer import region_grabber, image_search, image_search_area
from jaguabot.libraries.image_analyzer import image_search, append_global_dict
from jaguabot.libraries.image_analyzer import STATUS_BAR_DICT, END_COORDS_DICT, START_COORDS_DICT

#rgb colors
COLOR_DICT = {'hp': [219, 79, 79],
              'hp_empty': [77, 90, 116],
              'hp_end_bar': [47, 51, 62],
              'hp_full': [100, 46, 49],
              'mp': [101, 98, 240],
              'mp_empty': [89, 95, 106],
              'mp_end_bar': [51, 52, 56],
              'mp_full': [83, 80, 192]}


def find_battle_list():
    """
    Get battle list coord from an image
    :return:
    """
    img = "../assets/imgs/battle/battlelist.png"
    assert os.path.exists(img)
    img_coord = image_search(img)
    if img_coord[0] != -1 and img_coord[1] != -1:
        return img_coord[0], img_coord[1]


def find_batte_list_button():
    """
    Battlelist button to open list
    Used only battlelist is closed
    :return:
    """
    img = "../assets/imgs/battle/battlelist_menu_bt.png"
    assert os.path.exists(img)
    img_coord = image_search(img)
    if img_coord[0] != -1 and img_coord[1] != -1:
        return img_coord[0], img_coord[1]


def find_hp_bar():
    """
    Search for the life bar
    :return:
    """
    img = "../assets/imgs/healthy/life.png  "
    assert os.path.exists(img)
    img_coord = image_search(img)
    if img_coord[0] != -1 and img_coord[1] != -1:
        return img_coord[0], img_coord[1]


def find_mp_bar():
    """
    Search for the mana bar
    :return:
    """
    img = "../assets/imgs/healthy/mana.png"
    assert os.path.exists(img)
    img_coord = image_search(img)
    if img_coord[0] != -1 and img_coord[1] != -1:
        return img_coord[0], img_coord[1]


def find_hungry_status():
    """
    Search for the mana bar
    :return:
    """
    img = "../assets/imgs/healthy/hungry.png"
    assert os.path.exists(img)
    img_coord = image_search(img)
    if img_coord[0] != -1 and img_coord[1] != -1:
        return img_coord[0], img_coord[1]


def find_life_bar_coord():
    """
    Search for the life bar, then add coordinates (begin, end) to a list
    :return:
    """
    image = "../assets/imgs/healthy/life.png"
    img = cv2.imread(image, 0)
    img_w, img_h = img.shape[::-1]
    x_end, y_end = pyautogui.size()
    x_start = (x_end / 5) * 4
    screen_shot = region_grabber((x_start, 0, x_end, y_end))
    coords_relative = image_search_area(image, x_start, 0, x_end, y_end, im=screen_shot)
    if coords_relative[0] is not -1:
        coords = [coords_relative[0] + x_start + img_w, coords_relative[1] + 5]  # add back offset
        hp_start = find_pixel_color(COLOR_DICT['hp'], COLOR_DICT['hp_full'], 0,
                                    coords[0], coords[1], x_end, y_end)
        if hp_start[0] is not -1:
            append_global_dict(START_COORDS_DICT, 'hp', hp_start)
            hp_end = find_pixel_color(COLOR_DICT['hp_end_bar'], COLOR_DICT['hp_full'], 0,
                                      hp_start[0], hp_start[1], x_end, y_end)
            if hp_end[0] is not -1:
                append_global_dict(END_COORDS_DICT, 'hp', hp_end)

def find_mana_bar_coord():
    """
    Search for the mana bar, then add coordinates (begin, end) to a list
    :return:
    """
    image = "../assets/imgs/healthy/mana.png"
    img = cv2.imread(image, 0)
    img_w, img_h = img.shape[::-1]
    x_end, y_end = pyautogui.size()
    x_start = (x_end / 5) * 4
    screen_shot = region_grabber((x_start, 0, x_end, y_end))
    coords_relative = image_search_area(image, x_start, 0, x_end, y_end, im=screen_shot)
    if coords_relative[0] is not -1:
        coords = [coords_relative[0] + x_start + img_w, coords_relative[1] + 5]  # add back offset
        mp_start = find_pixel_color(COLOR_DICT['mp'], COLOR_DICT['mp_full'], 0,
                                    coords[0], coords[1], x_end, coords[1]+1)
        if mp_start[0] is not -1:
            append_global_dict(START_COORDS_DICT, 'mp', mp_start)
            mp_end = find_pixel_color(COLOR_DICT['mp_end_bar'], COLOR_DICT['mp_full'], 0,
                                      mp_start[0], mp_start[1], x_end, y_end)
            if mp_end[0] is not -1:
                append_global_dict(END_COORDS_DICT, 'mp', mp_end)


def get_current(empty_key, deviation):
    start = START_COORDS_DICT[empty_key[0:2]]
    end = END_COORDS_DICT[empty_key[0:2]]
    color = COLOR_DICT[empty_key]
    if start != [] and end != []:
        current_px = find_pixel_color(color, COLOR_DICT[empty_key[0:2]+'_full'], deviation, start[0], start[1], end[0], start[1]+1)
        if current_px[0] is not -1:
            current_pc = pixels_to_percent(start[0], end[0], current_px[0])
            print(current_pc)
            return int(current_pc)
        return None


if __name__ == '__main__':
    import time
    start_time = time.time()
    find_life_bar_coord()
    find_mana_bar_coord()
    get_current('hp_empty', 10)
    get_current('mp_empty', 10)
    print("--- %s seconds ---" % (time.time() - start_time))