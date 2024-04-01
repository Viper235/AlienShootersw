from gamesprite import *
from random import randint


class Enemy(GameSprite):
    
    # Переменная, которая хранит в себе количество пропущенных противников
    lost: int = 0

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.window.get_height():
            self.rect.y = -40
            self.rect.x = randint(0, self.window.get_height())
            # Увеличиваем свойство класса,
            # которое отвечает за кол-во пропущенных противников
            Enemy.lost += 1
