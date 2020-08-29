from threading import Thread

from jaguabot.engine.auto_heal import HealPotion, ManaPotion

if __name__ == '__main__':
    a = HealPotion()
    a.start()