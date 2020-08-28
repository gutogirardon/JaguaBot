"""
Get Coordinates from user screen
"""
import os
import logging

from jaguabot.libraries.image_analyzer import image_search

def find_battle_list():
    """
    Get battle list coord from an image
    :return:
    """
    img = "../assets/imgs/battle/battlelist.png"
    assert os.path.exists(img)
    try:
        img_coord = image_search(img)
        return img_coord
    except Exception as e:
        logging.error(e)

def find_batte_list_button():
    """
    Battlelist button to open list
    Used only battlelist is closed
    :return:
    """
    img = "../assets/imgs/battle/battlelist_menu_bt.png"
    assert os.path.exists(img)
    try:
        img_coord = image_search(img)
        return img_coord
    except Exception as e:
        logging.error(e)

def find_hp_bar():
    """
    Search for the life bar
    :return:
    """
    img = "../assets/imgs/healthy/life.png"
    assert os.path.exists(img)
    try:
        img_coord = image_search(img)
        return img_coord
    except Exception as e:
        logging.error(e)

def find_mp_bar():
    """
    Search for the mana bar
    :return:
    """
    img = "../assets/imgs/healthy/mana.png"
    assert os.path.exists(img)
    try:
        img_coord = image_search(img)
        return img_coord
    except Exception as e:
        logging.error(e)

def find_hungry_status():
    """
    Search for the mana bar
    :return:
    """
    img = "../assets/imgs/healthy/hungry.png"
    assert os.path.exists(img)
    try:
        img_coord = image_search(img)
        return img_coord
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    import time
    for i in range(20):
        start_time = time.time()
        find_hungry_status()
        print("--- %s seconds ---" % (time.time() - start_time))