from settings import *
from pygame.sprite import Sprite,Group


class PowerUp(Sprite):
    def __init__(self):
        super().__init__()
        powerups = ["shield","life","poison"]
        self.current = choice(powerups)
        
        if self.current == "shield":
            self.image = pygame.image.load(path.join("assets","sprites","powerup","addshield.png"))
        elif self.current == "life":
            self.image = pygame.image.load(path.join("assets","sprites","powerup","addlife.png"))
        elif self.current == "poison":
            self.image = pygame.image.load(path.join("assets","sprites","powerup","poison.png"))
            
            

        self.rect = self.image.get_rect()
        self.rect.x = randint(60,SC_WIDTH-60)
        self.rect.y = -20
        
        
    def update(self):
        self.rect.y += 1
        


class PowerUpGenerator():
    def __init__(self,screen):
        self.display_surface = screen
        self.group = Group()
        
        self.last_time_drop = 0
        self.cooldown = 20000
        
    def generate_powerup(self):
            powerup = PowerUp()
            self.group.add(powerup)
    
    def update(self):
        now = pygame.time.get_ticks()
        if (now - self.last_time_drop >= self.cooldown):
            self.last_time_drop = now
            self.generate_powerup()
        self.group.update()
        self.group.draw(self.display_surface)
        
        
        
if __name__ == "__main__":
    pygame.init()
    
    test_surface = pygame.display.set_mode(SC_SIZE)
    pygame.display.set_caption("Test PowerUps")
    clock = pygame.Clock()
    
    powerups = PowerUpGenerator(test_surface)
    
    while True:
        spc_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_q):
                break
        
        test_surface.fill((30,30,30))
        
        powerups.update()
        pygame.display.update()

        clock.tick(60)
    
    pygame.quit()
    