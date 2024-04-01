from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(
            self,
            player_image: str,
            player_x: int,
            player_y: int,
            player_speed: int,
            window: Surface
            ) -> None:
        
        super().__init__()
        self.window = window
        self.image = transform.scale(image.load(player_image), (55,55))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        self.window.blit(self.image,(self.rect.x, self.rect.y))
