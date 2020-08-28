"""
Coordinate Finder
"""
import os
from collections import defaultdict
import time
import cv2
import pyautogui
import numpy as np

from jaguabot.engine.utils import pixels2percent
from jaguabot.libraries.image_search import imagesearch, region_grabber, imagesearcharea
from jaguabot.libraries.pixel_processor import find_pixel_color

COLOR_DICT = {'hp': [219, 79, 79],
              'hp_empty': [77, 90, 116],
              'hp_end_bar': [47, 51, 62],
              'hp_full': [100, 46, 49],
              'mp': [101, 98, 240],
              'mp_empty': [89, 95, 106],
              'mp_end_bar': [51, 52, 56],
              'mp_full': [83, 80, 192]}

START_COORDS_DICT = defaultdict(list)
END_COORDS_DICT = defaultdict(list)
STATUS_BAR_DICT = defaultdict(list)

def find_battle_list_coord():
    """
    Get battle list coord from an image
    :return:
    """
    bt_img = "../assets/imgs/battle/battlelist.png"
    assert os.path.exists(bt_img)
    retry = 0
    retries = 3

    while retry < retries:
        try:
            retry += 1
            bt_coord = imagesearch(bt_img)
            if bt_coord[0] != -1:
                pyautogui.moveTo(bt_coord[0], bt_coord[1])
                break
            else:
                open_battle_list_coord()
        except Exception as e:
            print(f"Não foi possível encontrar o battle list {e}")

def open_battle_list_coord():
    """
    Open the battle list if its closed
    :return:
    """
    bt_button = "../assets/imgs/battle/battlelist_menu_bt.png"
    assert os.path.exists(bt_button)
    try:
        bt_menu_coord = imagesearch(bt_button)
        if bt_menu_coord[0] != -1:
            pyautogui.moveTo(bt_menu_coord[0], bt_menu_coord[1])
            pyautogui.click(bt_menu_coord[0], bt_menu_coord[1])
    except Exception as e:
        raise e

def find_life_bar_coord():
    """
    Search for the life bar, then add coordinates (begin, end) to a list
    :return:
    """
    life_img = "../assets/imgs/healthy/life.png"
    assert os.path.exists(life_img)

    image = "../assets/imgs/healthy/life.png"
    img = cv2.imread(image, 0)
    img_w, img_h = img.shape[::-1]
    x_end, y_end = pyautogui.size()
    x_start = (x_end / 5) * 4
    screen_shot = region_grabber((x_start, 0, x_end, y_end))
    coords_relative = imagesearcharea(image, x_start, 0, x_end, y_end, im=screen_shot)
    if coords_relative[0] is not -1:
        coords = [coords_relative[0] + x_start + img_w, coords_relative[1] + 5]  # add back offset
        hp_start = find_pixel_color(COLOR_DICT['hp'], COLOR_DICT['hp_full'], 0,
                                    coords[0], coords[1], x_end, y_end)
        if hp_start[0] is not -1:
            append_dict(START_COORDS_DICT, 'hp', hp_start)
            hp_end = find_pixel_color(COLOR_DICT['hp_end_bar'], COLOR_DICT['hp_full'], 0,
                                      hp_start[0], hp_start[1], x_end, y_end)
            if hp_end[0] is not -1:
                append_dict(END_COORDS_DICT, 'hp', hp_end)


def get_curr(empty_key, deviation):
    start = START_COORDS_DICT[empty_key[0:2]]
    end = END_COORDS_DICT[empty_key[0:2]]
    color = COLOR_DICT[empty_key]
    if start != [] and end != []:
        current_px = find_pixel_color(color, COLOR_DICT[empty_key[0:2]+'_full'], deviation, start[0], start[1], end[0], start[1]+1)
        if current_px[0] is not -1:
            current_pc = pixels2percent(start[0], end[0], current_px[0])
            print(current_pc)
            return int(current_pc)
        return None
    else:
        print("Couldn't find start or end anchor for hp/mp, try restarting. \n \
        Are 'show status bar' toggled in Tibia options? \n \
        Advanced settings, Interface -> HUD at the bottom. \n \n \
        if you are running several monitors its possible we are looking at another monitor.")

def append_dict(dict, key, values):
    for item in values:
        if item not in dict[key]:
            dict[key].append(item)


if __name__ == '__main__':
    start_time = time.time()
    #find_battle_list_coord()
    find_life_bar_coord()
    hp = get_curr('hp_empty', 10)
    print("--- %s seconds ---" % (time.time() - start_time))


