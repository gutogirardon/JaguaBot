import pyautogui

from jaguabot.engine.position_finder import find_batte_list_button

def open_battle_list_coord():
    """
    Open the battle list if its closed
    :return:
    """
    try:
        pos_x, pox_y = find_batte_list_button()
        pyautogui.moveTo(pos_x, pox_y)
        pyautogui.click(pos_x, pox_y)
    except Exception as e:
        print("Cannot open battle list!")




if __name__ == '__main__':
    pass
