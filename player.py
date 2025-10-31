from settings import *
from pygame.sprite import Sprite,Group
from rockets import PlayerRocket


class Player(Sprite):
    def __init__(self, screen:pygame.Surface,x, y):
        super().__init__()
        self.display_surface = screen
        self.image = pygame.image.load(path.join("assets","sprites","player.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.velocity = PLAYER_VELOCITY
        
        self.last_time_shoot = 0
        self.cooldown = PLAYER_ROCKET_COOLDOWN

        self.group_rockets = Group()
        
        self.shield = False
        self.shield_image = pygame.image.load(path.join("assets","sprites","powerup","shield.png"))
        self.shield_rect = self.shield_image.get_rect()
        self.shield_timer = 0
        self.shield_duration = PLAYER_SHIELD_DURATION
        
    def update(self,space_clicked:bool=False,shield:bool = False):
        #print(f"shield: {shield}")
        if shield == True:
            self.shield = True
        self.movement()
        if space_clicked and self.check_rocket_cooldown():
            self.last_time_shoot = pygame.time.get_ticks()
            self.shoot()
        self.group_rockets.update()
        self.group_rockets.draw(self.display_surface)
        
        
        if self.shield and (self.shield_timer <= self.shield_duration):
            #print(f"shiled duration: {self.shield_timer}/{self.shield_duration}")
            self.shield_rect.x = self.rect.x - 12
            self.shield_rect.y = self.rect.y - 10
            self.display_surface.blit(self.shield_image,self.shield_rect)
            self.shield_timer += 1
            
        else:
            self.shield = False
            self.shield_timer = 0
        
    def return_shield_state(self):
        return self.shield
    
    def movement(self):
        key = pygame.key.get_pressed()
        if key[K_w] and self.rect.y > 0:
            self.rect.y -= self.velocity
        if key[K_s] and self.rect.y < SC_HEIGHT-self.rect.h:
            self.rect.y += self.velocity
        if key[K_a] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if key[K_d] and self.rect.x < SC_WIDTH-self.rect.w:
            self.rect.x += self.velocity
    
    
    def shoot(self):
        """we assume shoot control key is clicked\n
        must be controlled with pygame.event cause pressing keep making object i guess"""
        rocket = PlayerRocket(x=self.rect.centerx-4,y=self.rect.centery)
        self.group_rockets.add(rocket)
        soundPlayerShoot.play()
        
    
    def check_rocket_cooldown(self):
        """returns True if not cooldown, False if cooldown"""
        current_time = pygame.time.get_ticks()
        if (self.last_time_shoot == 0) or (current_time - self.last_time_shoot > self.cooldown):            
            return True
        return False
        
        
        
        
        

if __name__ == "__main__":
    pygame.init()
    
    test_surface = pygame.display.set_mode(SC_SIZE)
    pygame.display.set_caption("Test Player")
    clock = pygame.Clock()
    player = Player(screen= test_surface,x=SC_WIDTH//2, y=SC_HEIGHT//2)
    
    group = pygame.sprite.Group()
    group.add(player)
    
    while True:
        spc_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_q):
                break
            if event.type == KEYDOWN and event.key == K_SPACE:
                    spc_clicked = True
        
        test_surface.fill((30,30,30))
        group.update(spc_clicked)
        group.draw(test_surface)
        pygame.display.update()

        clock.tick(60)
    
    pygame.quit()