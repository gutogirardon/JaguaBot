import time
from threading import Thread

from jaguabot.engine.position_finder import find_life_bar_coord, find_mana_bar_coord, get_current
from jaguabot.libraries.keyboard_actions import Key, press_key

class HealPotion(Thread):
    def __init__(self):
        """
        pass
        """
        Thread.__init__(self)
        self.running = True

    def run(self):
        """
        Parametrizar a tecla de cura
        Parametrizar a porcentagem de cura
        @todo melhorar description / ingles
        :return:
        """
        # Get data from life and update dict
        while self.running:
            find_life_bar_coord()
            life_percentage = get_current('hp_empty', 10)
            if life_percentage and life_percentage < 60:
                press_key(Key.F1)

class ManaPotion(Thread):
    def __init__(self):
        """
        pass
        """
        Thread.__init__(self)
        self.running = True

    def run(self):
        """
        Parametrizar a tecla de cura
        Parametrizar a porcentagem de cura
        @todo melhorar description / ingles
        :return:
        """
        # Get data from life and update dict
        while self.running:
            find_mana_bar_coord()
            mana_percentage = get_current('mp_empty', 10)
            if mana_percentage and mana_percentage < 70:
                press_key(Key.F2)

if __name__ == '__main__':
    start_time = time.time()
    a = HealPotion()
    b = ManaPotion()
    a.start()
    b.start()
    a.join()
    b.join()

    # auto_heal()
    print("--- %s seconds ---" % (time.time() - start_time))
