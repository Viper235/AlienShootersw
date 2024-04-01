from gamesprite import *

class Bullet(GameSprite):
    #Вызывается во время каждого кадра
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    