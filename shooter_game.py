#Создай собственный Шутер!

from pygame import *
from random import randint, choice

# Импортируем написанные нами классы
from gamesprite import GameSprite
from player import Player
from enemy import Enemy

# Переменная, которая хранит в себе счет игрока
win_w = 700
win_h = 500
window = display.set_mode((win_w, win_h))
display.set_caption('Allien Shooter')

#Создаем фоновую музыку
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

gameoverSound = mixer.Sound('zw_gameover.mp3')

#шрифты и надписи
font.init()
font2 = font.Font(None, 36)

score = 0 #сбито кораблей

clock = time.Clock()

FPS = 60

#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#Основной цикл игры:
game = True #флаг сбрасывается кнопкой закрытия окна
# Создаем фон
bg = transform.scale(image.load('galaxy.jpg'),(win_w,win_h))
# Создаем нашего игрока
player = Player('rocket.png',win_w // 2 - 40, win_h - 60, 3, window)
# Создаем группу спрайтов врагов
enemies = sprite.Group()


speeds = [1,1,2,2,3]

for i in range(5):
    enemies.add(
        Enemy(
            'ufo.png',randint( 0, win_w), -40, speeds[i], window
        )
    ) 

while game:
    #
    window.blit(bg, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    #Пока не проиграли
    if not finish:
        #Сколько сбито
        text_score = font2.render(f'Сбито:{score}', 1, (255,255,255))

        window.blit(text_score, (10,20))

        #Сколько мы пропустили
        text_lost = font2.render(f'Пропущено:{Enemy.lost}', 1, (255,255,255))

        window.blit(text_lost, (10,50))


        colEnemies: dict[Enemy,list] = sprite.groupcollide(enemies, player.bullets,True,True)

        for enemy in colEnemies:
            score += 1
                                 
            enemies.add(Enemy(choice(['ufo.png', 'asteroid.png']), randint(-10,win_w), 0, choice(speeds), window))
        
        #Список столкновения игрока с врагом
        colplayer = sprite.spritecollide(player, enemies, False)

        if colplayer:
            finish = True
            mixer.music.stop()
            gameoverSound.play(loops= 0)

        #Проигрыш
        if colplayer or Enemy.lost >= 10:
            finish = True
            mixer.music.stop()
            gameoverSound.play()


        #Меняем положение 
        player.update()
        enemies.update()
        player.bullets.update()
        
        player.bullets.draw(window)
        player.reset()
        enemies.draw(window)
        #Обновляем картинку на экране

    if finish:
        gameoverText = font2.render('GAME OVER', True,(255,255,255))
        go_rect = gameoverText.get_rect()
        window.blit(gameoverText, (win_w // 2 - go_rect.width //2, win_h // 2 - go_rect.height //2))

    display.update()

    clock.tick(60)