from settings import *
from pygame.sprite import Sprite,Group
from rockets import  AlienGreenRocket,AlienCyanRocket



class Test(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(path.join("assets","sprites","player.png"))
        self.rect = self.image.get_rect()
        self.rect.x = SC_WIDTH//2
        self.rect.y = SC_HEIGHT - 70
        
    def update(self):
        key = pygame.key.get_pressed()
        if key[K_w]:
            self.rect.y -= 4
        if key[K_s]:
            self.rect.y += 4
        if key[K_a]:
            self.rect.x -= 4
        if key[K_d]:
            self.rect.x += 4
        
            

class AlienRed(Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load(path.join("assets","sprites","aliens","alien-red.png"))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)
        self.velocity = ALIEN_RED_VELOCITY
        
    def update(self):
        self.movement()
        if self.rect.y > SC_HEIGHT + 16:
            self.kill()
    
    def movement(self):
        self.rect.y += self.velocity
        
      
        
class AlienGreen(Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load(path.join("assets","sprites","aliens","alien-green.png"))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)
        
        # to make movement look grid by grid
        self.frame_movement = FPS
        self.frame_current = 0
        
        self.side_steps = ALGREEN_SIDE_STEPS
        self.down_steps = ALGREEN_FIRST_STEPS
        self.swap_direction = False
        
        self.velocity = ALIEN_GREEN_VELOCITY
        
    def update(self):
        self.frame_current += 1
        if self.frame_current == self.frame_movement:
            self.movement()
            self.frame_current = 0
        if self.rect.y > SC_HEIGHT:
            self.kill()
        
    def movement(self):
        if self.down_steps > 0:
            self.rect.y += self.velocity
            self.down_steps -= 1
        else:            
            if self.swap_direction:
                self.rect.x += self.velocity
            else:
                self.rect.x -= self.velocity
            self.side_steps -= 1
            if self.side_steps == 0:
                self.rect.y += self.velocity
                self.side_steps = ALGREEN_SIDE_STEPS
                self.swap_direction = not self.swap_direction
            
    def shoot(self):
        rocket = AlienGreenRocket(self.rect.x,self.rect.y)
        soundAlienShoot.play()
        return rocket
   
   
   
         
class AlienCyan(Sprite):
    def __init__(self,x,y,movement):
        super().__init__()
        self.movement = movement
        self.image = pygame.image.load(path.join("assets","sprites","aliens","alien-cyan.png"))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)

        self.velocity = ALIEN_CYAN_VELOCITY_MIN
        
        self.rtl_ltr_move = {"topToBot":{"dx":-1,"dy":1},"botToTop":{"dx":1,"dy":-1}}
        self.ltr_rtl_move = {"topToBot":{"dx":1,"dy":1},"botToTop":{"dx":-1,"dy":-1}}
        
        self.swap_direction = False
        
    
    def update(self):
        if self.movement == "ltr":
            self.movement_ltr()
        elif self.movement == "rtl":
            self.movement_rtl()
        
        
    def movement_rtl(self):
        if not self.swap_direction:
            dx = self.rtl_ltr_move["topToBot"]["dx"]
            dy = self.rtl_ltr_move["topToBot"]["dy"]
            
            self.rect.x += dx* self.velocity
            self.rect.y += dy* self.velocity
            
            if self.rect.bottom >= SC_HEIGHT - 200:
                self.swap_direction = not self.swap_direction
                self.velocity = ALIEN_CYAN_VELOCITY_MAX
                
        elif self.swap_direction:
            dx = self.rtl_ltr_move["botToTop"]["dx"]
            dy = self.rtl_ltr_move["botToTop"]["dy"]
            
            self.rect.x += dx* self.velocity
            self.rect.y += dy* self.velocity
            
            if self.rect.top <= 20:
                self.swap_direction = not self.swap_direction
                self.velocity = ALIEN_CYAN_VELOCITY_MIN
                
                
    def movement_ltr(self):
        if not self.swap_direction:
            dx = self.ltr_rtl_move["topToBot"]["dx"]
            dy = self.ltr_rtl_move["topToBot"]["dy"]
            
            self.rect.x += dx* self.velocity
            self.rect.y += dy* self.velocity
            
            if self.rect.bottom >= SC_HEIGHT - 200:
                self.swap_direction = not self.swap_direction
                self.velocity = ALIEN_CYAN_VELOCITY_MAX
                
        elif self.swap_direction:
            dx = self.ltr_rtl_move["botToTop"]["dx"]
            dy = self.ltr_rtl_move["botToTop"]["dy"]
            
            self.rect.x += dx* self.velocity
            self.rect.y += dy* self.velocity
            
            if self.rect.top <= 20:
                self.swap_direction = not self.swap_direction
                self.velocity = ALIEN_CYAN_VELOCITY_MIN
    
    def shoot(self):
        rocket = AlienCyanRocket(self.rect.x,self.rect.y)
        soundAlienShoot.play()
        return rocket




class UnitCyanGenerator():
    def __init__(self,screen):
        self.display_surface = screen
        self.group_cyan = Group()
        self.group_rocket = Group()
        
        
        self.generate_count = ALCYAN_GENCOUNT

        
        self.last_time_spawned = 0
        self.spawncooldown = ALCYAN_COOLDOWN
        
        self.last_time_shot = 0
        self.rocketcooldown = ALCYAN_ROCKET_COOLDOWN
    
    def rockets(self):
        if self.group_cyan.sprites() != []:
            who_shot = choices(self.group_cyan.sprites() ,k = 6)
            for alien in who_shot:
                self.group_rocket.add(alien.shoot())
    
        
    def generate_left_side(self):
        x ,y = 0, -40
        for i in range(6):
            alien = AlienCyan(x = x, y= y, movement = "ltr")
            self.group_cyan.add(alien)
            x -= 20
            y -= 20
        
    def generate_right_side(self):
        x ,y = SC_WIDTH, -40
        for i in range(6):
            alien = AlienCyan(x = x, y= y, movement = "rtl")
            self.group_cyan.add(alien)
            x += 20
            y -= 20
        
    def generate_both_sides(self):
        self.generate_right_side()
        self.generate_left_side()
    
    def generate_random_pattern(self):
        patterns = ["lef-side","right-side","both-side"]  
        patt = choice(patterns)
        
        if patt == "left-side":
            self.generate_left_side()
        elif patt == "right-side":
            self.generate_right_side()
        elif patt == "both-side":
            self.generate_both_sides()
        else: # in some cases when i execute this class does not generate anything idk the reason yet
            self.generate_both_sides()

        
    def update(self):
        if self.generate_count <= 0:
            return False
        if self.generate_count > 0:
            
            now = pygame.time.get_ticks()
            if now - self.last_time_shot >= self.rocketcooldown: 
                self.last_time_shot = now
                self.rockets()    
                
            if (self.last_time_spawned==0) or(now - self.last_time_spawned >= self.spawncooldown):
                self.last_time_spawned = now 
                self.generate_random_pattern()
                self.generate_count -= 1
                
            self.group_cyan.update()
            self.group_cyan.draw(self.display_surface)
            self.group_rocket.update()
            self.group_rocket.draw(self.display_surface)
        
   
        return True
       
       
class UnitGreenGenerator():
    def __init__(self,screen):
        self.display_surface = screen
        self.rows = 12
        self.cols = 30

        self.group_green = Group()
        self.group_rocket = Group()
        
        self.horde_count = 1
        
        self.last_time_shot = 0
        self.cooldown = ALGREEN_ROCKET_COOLDOWN
    
    
    def rockets(self):
        who_shot = choices(self.group_green.sprites() ,k = 10)
        for alien in who_shot:
            self.group_rocket.add(alien.shoot())
        
    def generate_rows(self,rows=2,cols=3):
        resetx = x = SC_WIDTH - 34
        y = 30
        for row in range(rows):
            for col in range(cols):
                alien = AlienGreen(x=x,y= y)
                self.group_green.add(alien)
                x -= 20
            x = resetx
            y -= 20

    def update(self):    
        if self.horde_count > 0:
            self.generate_rows(self.rows,self.cols)
            self.horde_count -= 1
            
        if self.group_green.sprites() == []:
            return False
            
        now = pygame.time.get_ticks()
        if now - self.last_time_shot >= self.cooldown: 
            self.last_time_shot = now
            self.rockets()    
       
        self.group_green.update()
        self.group_green.draw(self.display_surface)
        self.group_rocket.update()
        self.group_rocket.draw(self.display_surface)
        return True
        
        
        
        
                
class UnitRedGenerator():
    def __init__(self,screen):
        self.display_surface = screen
        self.group_red = Group()
        
        self.patterns = ["3units","5units","rows"]
        
        self.last_time_spawned = 0
        self.cooldown = ALRED_COOLDOWN_MAX
        self.generate_count = 10
    
    def generate_3units(self):
        alien1 = AlienRed(x=randint(ALRED_SPAWN_XMIN,ALRED_SPAWN_XMAX),y=-80)
        alien2 = AlienRed(x=alien1.rect.x-16,y=-80-16)
        alien3 = AlienRed(x=alien1.rect.x+16,y=-80-16)              
        self.group_red.add(alien1,alien2,alien3)
    
    def generate_5units(self):
        alien1 = AlienRed(x=randint(ALRED_SPAWN_XMIN,ALRED_SPAWN_XMAX),y=-80)
        alien2 = AlienRed(x=alien1.rect.x-16,y=-80-16)
        alien3 = AlienRed(x=alien1.rect.x+16,y=-80-16)        
        alien4 = AlienRed(x=alien1.rect.x-32,y=-80-32)        
        alien5 = AlienRed(x=alien1.rect.x+32,y=-80-32)        
        self.group_red.add(alien1,alien2,alien3,alien4,alien5)
        
    def generate_rows(self,rows=2,cols=3):
        resetx = x = randint(ALRED_SPAWN_XMIN,ALRED_SPAWN_XMAX)
        y = -60
        for row in range(rows):
            for col in range(cols):
                alien = AlienRed(x=x,y= y)
                self.group_red.add(alien)
                x += 20
            x = resetx
            y -= 20
        
    def generate_random_pattern(self):
        patt = choice(self.patterns)
        
        if patt == "3units":
            self.generate_3units()
        if patt == "5units":
            self.generate_5units()
        if patt == "rows":
            self.generate_rows()

        
    def update(self):
        if self.generate_count <= 0:
            return False
        if self.generate_count > 0:
            now = pygame.time.get_ticks()
            if (self.last_time_spawned == 0) or (now - self.last_time_spawned >= self.cooldown):
                self.last_time_spawned = now
                self.generate_random_pattern()
                self.generate_count -= 1
                self.cooldown -= 200
                if self.cooldown < ALRED_COOLDOWN_MIN:
                    self.cooldown = ALRED_COOLDOWN_MIN
            self.group_red.update()
            self.group_red.draw(self.display_surface)
        
        return True
                
        



# # NOTE test UnitCyanGenerator
# if __name__ == "__main__":
#     pygame.init()
#     test_surface = pygame.display.set_mode(SC_SIZE)
#     pygame.display.set_caption("Test Aliens")
#     clock = pygame.Clock()


#     groupcyan = UnitCyanGenerator(test_surface)

#     alien = AlienCyan(x=20,y=-20,movement="rtl")
#     group = Group()
#     group.add(alien)
        
#     #test
#     player = Test(test_surface)
#     group_player = Group()
#     group_player.add(player)

   
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT or (event.type == KEYDOWN and event.type == K_q):
#                 break
#         test_surface.fill((30,30,30))       
        
#         groupcyan.update()
#         # test
#         group_player.update()
#         group_player.draw(test_surface)
#         pygame.display.update()
        
        
#         clock.tick(60)
#     pygame.quit()

# # NOTE test UnitGreenGenerator
# if __name__ == "__main__":
#     pygame.init()
#     test_surface = pygame.display.set_mode(SC_SIZE)
#     pygame.display.set_caption("Test Guide Man")
#     clock = pygame.Clock()

#     # group
#     groupgreen = UnitGreenGenerator(test_surface)
        
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT or (event.type == KEYDOWN and event.type == K_q):
#                 break
#         test_surface.fill((30,30,30))       
        
#         #group.update\
#         groupgreen.update()
            
#         pygame.display.update()
#         clock.tick(60)
#     pygame.quit()

# NOTE test UnitRedGenerator
if __name__ == "__main__":
    pygame.init()
    test_surface = pygame.display.set_mode(SC_SIZE)
    pygame.display.set_caption("Test Guide Man")
    clock = pygame.Clock()

    groupred = UnitRedGenerator(test_surface)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_q):
                break
        test_surface.fill((30,30,30))       
        groupred.update()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()