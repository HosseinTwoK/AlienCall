from settings import *
from pygame.sprite import Sprite,Group

class PlayerRocket(Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.image = pygame.image.load(path.join("assets","sprites","rocket","rocket-player.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = PLAYER_ROCKET_VELOCITY
        
    def update(self):
        self.rect.y -= self.velocity
        
        if self.rect.y <= 0:
            self.kill() # destroy self instance
        

class AlienGreenRocket(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(path.join("assets", 'sprites', "rocket", "rocket-red.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = ALGREEN_ROCKET_VELOCITY
        
    def update(self):
        self.rect.y += self.velocity
        
        if self.rect.y >= SC_HEIGHT:
            self.kill()
        
        
        
class AlienCyanRocket(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(path.join("assets", 'sprites', "rocket", "rocket-cyan.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = ALGREEN_ROCKET_VELOCITY
        
    def update(self):
        self.rect.y += self.velocity
        
        if self.rect.y >= SC_HEIGHT:
            self.kill()
        
        

        
