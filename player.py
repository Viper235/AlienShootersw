from gamesprite import *
from bullet import Bullet

class Player(GameSprite):

    bullets = sprite.Group()
    #Время последнего выстрела
    last_bullet_time = time.get_ticks()
    #
    bullet_delay: int = 400

    # Создаем звук выстрела 
    mixer.init()
    fire_sound = mixer.Sound('fire.ogg')


    def update(self):
        '''
        Реагирует на нажатие клавишь
        '''

        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT]:
            self.rect.x += self.speed
        if key_pressed[K_SPACE]:
            self.fire()
        #Левый край
        if self.rect.right < 0:
            self.rect.x = self.window.get_width() - 10
        if self.rect.x >= self.window.get_width() :
            self.rect.x = 0 

    def fire(self):

        #Сейчас
        now = time.get_ticks()
        # выарвыаорвыоар
        if now - self.last_bullet_time >= self.bullet_delay:
            self.bullets.add(Bullet('bullet.png',self.rect.x,self.rect.top, 6, self.window))

            #Фиксируем время последнего выстрела
            self.last_bullet_time = now
            self.fire_sound.play()