from settings import *
from player import Player
from powerup import PowerUpGenerator
from pygame.sprite import Group
from ui import UI
from wave import Waves
from alienboss import ComingSoon


class Game():
    """ controls game assets and game logics"""
    def __init__(self,screen:pygame.Surface):
        self.fontLarge = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),50)
        self.fontSmall = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),22)
        
        self.display_surface = screen
        
        self.player_lives = PLAYER_MAX_LIVES
        self.player_score = 0
        
        self.player_shield = False
        
        self.shield = False
        
        self.BossFight = ComingSoon(self.display_surface)
        self.ui = UI(screen = self.display_surface, lives = self.player_lives)
        self.wave = Waves(screen= self.display_surface)
        self.w = 0

        self.timer = 0
        self.wave_cooldown = 2000
        
        self.game_finished = False
        self.game_pause = False
        self.game_over = False
    

    
    def reset(self):
        del self.player_group
        del self.player
        del self.powerup 
        del self.ui
        del self.wave
        del self.BossFight
        
        self.player_lives = PLAYER_MAX_LIVES
        self.player_score = 0
      
        self.game_finished = False

        self.BossFight = ComingSoon(self.display_surface)
        self.ui = UI(screen = self.display_surface, lives = self.player_lives)
        self.wave = Waves(screen= self.display_surface)
        self.w = 0
        self.create_groups()
        
        
    def won(self):
        # Note Complete
        pos = (0,0)
        size = SC_SIZE
        
        overlay = pygame.Surface(size= size)
        overlay.fill(CLR_GOLD)
        overlay.set_alpha(5)
        
        text_over = self.fontLarge.render("YOU WON",True,CLR_DBLUE)
        text_over_rect = text_over.get_rect()
        text_over_rect.center = POS_CENTER
        text_over_rect.y -= 200
        text_quit = self.fontSmall.render("press \"Q\" to quit", True, CLR_DBLUE)
        text_quit_rect = text_quit.get_rect()
        text_quit_rect.center = POS_CENTER
        text_quit_rect.y -= 100
        text_reset = self.fontSmall.render("press \"R\" to restart", True, CLR_DBLUE)
        text_reset_rect = text_reset.get_rect()
        text_reset_rect.center = POS_CENTER
        
        
        while self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    self.game_over = False
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.game_pause = False
                        self.reset()
                        return True
                    
            self.display_surface.blit(overlay,pos)
            self.display_surface.blit(text_over,text_over_rect)
            self.display_surface.blit(text_quit,text_quit_rect)
            self.display_surface.blit(text_reset,text_reset_rect)
            pygame.display.update()
        
        
    def over(self):
        pos = (0,0)
        size = SC_SIZE
        
        overlay = pygame.Surface(size= size)
        overlay.fill(CLR_RED)
        overlay.set_alpha(2)
        
        text_over = self.fontLarge.render("GAMEOVER",True,CLR_DBLUE)
        text_over_rect = text_over.get_rect()
        text_over_rect.center = POS_CENTER
        text_over_rect.y -= 200
        text_quit = self.fontSmall.render("press \"Q\" to quit", True, CLR_DBLUE)
        text_quit_rect = text_quit.get_rect()
        text_quit_rect.center = POS_CENTER
        text_quit_rect.y -= 100
        text_reset = self.fontSmall.render("press \"R\" to restart", True, CLR_DBLUE)
        text_reset_rect = text_reset.get_rect()
        text_reset_rect.center = POS_CENTER
        
        
        while self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    self.game_over = False
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.game_pause = False
                        self.reset()
                        return True
                    
            self.display_surface.blit(overlay,pos)
            self.display_surface.blit(text_over,text_over_rect)
            self.display_surface.blit(text_quit,text_quit_rect)
            self.display_surface.blit(text_reset,text_reset_rect)
            pygame.display.update()
        
        
    def pause(self):
        pos = (0,0)
        size = SC_SIZE
        
        overlay = pygame.Surface(size= size)
        overlay.fill(CLR_WHITE)
        overlay.set_alpha(2)
        
        text_pause = self.fontLarge.render("PAUSE",True,CLR_DBLUE)
        text_pause_rect = text_pause.get_rect()
        text_pause_rect.center = POS_CENTER
        text_pause_rect.y -= 200
        text_quit = self.fontSmall.render("press \"Q\" to quit", True, CLR_DBLUE)
        text_quit_rect = text_quit.get_rect()
        text_quit_rect.center = POS_CENTER
        text_quit_rect.y -= 100
        text_reset = self.fontSmall.render("press \"R\" to restart", True, CLR_DBLUE)
        text_reset_rect = text_reset.get_rect()
        text_reset_rect.center = POS_CENTER
        text_unpause = self.fontSmall.render("press \"ESC\" to unpause", True, CLR_DBLUE)
        text_unpause_rect = text_unpause.get_rect()
        text_unpause_rect.center = POS_CENTER
        text_unpause_rect.y += 100
        
        
        while self.game_pause:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    self.game_pause = False
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_pause = False
                        return True
                    if event.key == K_r:
                        self.game_pause = False
                        self.reset()
                        return True
                        

                    
            self.display_surface.blit(overlay,pos)
            self.display_surface.blit(text_pause,text_pause_rect)
            self.display_surface.blit(text_quit,text_quit_rect)
            self.display_surface.blit(text_unpause,text_unpause_rect)
            self.display_surface.blit(text_reset,text_reset_rect)
            pygame.display.update()

            
    
    def load_assets(self):
        self.image_background = pygame.image.load(path.join("assets", "sprites", "background.png"))
        self.rect_background = self.image_background.get_rect()
        
    def blit_assets(self):
        self.display_surface.blit(self.image_background, self.rect_background)
        
        
    def create_groups(self):
        self.player = Player(screen=self.display_surface,x= SC_WIDTH//2, y = SC_HEIGHT - 128)
        self.player_group = Group()
        self.player_group.add(self.player)

        self.powerup = PowerUpGenerator(self.display_surface)
        
        
    def update_objects(self,key):
        if key == "ESC":
            self.game_pause = True
        
        # NOTE Hold os Tap the button (Hold is better i guess)
        #if key == "SPACE":
        keys = pygame.key.get_pressed() 
        if keys[K_SPACE]:
            shoot = True
        else:
            shoot = False
        self.player_group.update(space_clicked = shoot,shield = self.shield)
        self.shield = self.player.return_shield_state()
        self.player_group.draw(self.display_surface)
        
        self.powerup.update()
        
    
    def check_powerup_collision(self):
        collided = pygame.sprite.groupcollide(self.powerup.group, self.player_group, True, False)
        for power in collided:
            if power.current == "poison":
                soundPlayerDamaged.play() 
                self.player_lives = self.ui.remove_life()
                power.current = ""
            elif power.current == "life":
                soundPowerUp.play()
                self.player_lives = self.ui.add_life()
                power.current = ""
            elif power.current == "shield":
                soundPowerUp.play()
                self.shield = True
                power.current = ""
            print(f"player lives: {self.player_lives}")
    
    def collision_danger_check(self):
        # get hit
        if pygame.sprite.groupcollide(self.player_group, self.wave.units_red.group_red, False, True):
            self.ui.remove_life()
            self.player_lives -= 1
            soundPlayerDamaged.play()
        if pygame.sprite.groupcollide(self.player_group, self.wave.units_two_red.group_red, False, True):
            self.ui.remove_life()
            self.player_lives -= 1
            soundPlayerDamaged.play()

        if pygame.sprite.groupcollide(self.player_group, self.wave.units_cyan.group_cyan, False, True):
            self.ui.remove_life()
            self.player_lives -= 1  
            soundPlayerDamaged.play()
        if pygame.sprite.groupcollide(self.player_group, self.wave.units_two_cyan.group_cyan, False, True):
            self.ui.remove_life()
            self.player_lives -= 1 
            soundPlayerDamaged.play()
        
        if pygame.sprite.groupcollide(self.player_group, self.wave.units_green.group_green, False, True):
            self.ui.remove_life()
            self.player_lives -= 1 
            soundPlayerDamaged.play()
        if pygame.sprite.groupcollide(self.player_group, self.wave.units_two_green.group_green, False, True):
            self.ui.remove_life()
            self.player_lives -= 1 
            soundPlayerDamaged.play()
        
        # get shot
        if pygame.sprite.groupcollide(self.player_group, self.wave.units_green.group_rocket, False, True):
            self.ui.remove_life()
            self.player_lives -= 1 
            soundPlayerDamaged.play()
        if pygame.sprite.groupcollide(self.player_group, self.wave.units_two_green.group_rocket, False, True):
            self.ui.remove_life()
            self.player_lives -= 1 
            soundPlayerDamaged.play()
            
        if pygame.sprite.groupcollide(self.player_group, self.wave.units_cyan.group_rocket, False, True):
            self.ui.remove_life()
            self.player_lives -= 1
            soundPlayerDamaged.play() 
        if pygame.sprite.groupcollide(self.player_group, self.wave.units_two_cyan.group_rocket, False, True):
            self.ui.remove_life()
            self.player_lives -= 1
            soundPlayerDamaged.play() 
              
    def collision_checks(self):
        # player rockets kill green alien
        if pygame.sprite.groupcollide(self.player.group_rockets, self.wave.units_green.group_green, True, True):
            self.player_score += ALIEN_GREEN_SCORE
            self.ui.add_score(ALIEN_GREEN_SCORE)
        if pygame.sprite.groupcollide(self.player.group_rockets, self.wave.units_two_green.group_green, True, True):
            self.player_score += ALIEN_GREEN_SCORE
            self.ui.add_score(ALIEN_GREEN_SCORE)
        
        # player rocket kill cyan alien
        if pygame.sprite.groupcollide(self.player.group_rockets, self.wave.units_cyan.group_cyan, True, True):
            self.player_score += ALIEN_CYAN_SCORE
            self.ui.add_score(ALIEN_CYAN_SCORE)
        if pygame.sprite.groupcollide(self.player.group_rockets, self.wave.units_two_cyan.group_cyan, True, True):
            self.player_score += ALIEN_CYAN_SCORE
            self.ui.add_score(ALIEN_CYAN_SCORE)
   
        # player rocket kill red alien
        if pygame.sprite.groupcollide(self.player.group_rockets, self.wave.units_red.group_red, True, True):
            self.player_score += ALIEN_RED_SCORE
            self.ui.add_score(ALIEN_RED_SCORE)
        if pygame.sprite.groupcollide(self.player.group_rockets, self.wave.units_two_red.group_red, True, True):
            self.player_score += ALIEN_RED_SCORE
            self.ui.add_score(ALIEN_RED_SCORE)
            
            
    def wave_control(self):
        done = False
        
        if self.w == 0:
            self.ui.update_wave(1)
            
            done = self.wave.wave_first()
            if done:
                self.w = 1
                

        elif self.w == 1:
            
            self.ui.update_wave(2)
            done = self.wave.wave_second(True)
            if done:
                self.w = 2
                
        elif self.w == 2:
            
            self.ui.update_wave(3)
            done = self.wave.wave_third(True)
            if done:
                self.w = 3
                
        elif self.w == 3:
            
            self.ui.update_wave(4)
            done = self.wave.wave_fourth(True)
            if done:
                self.w = 4 # TODO
                
        elif self.w == 4:
            
            self.BossFight.show_end()
            self.game_finished = True
            
            
                
            
    def update(self,key):
        """updates the logic and display\n
        return False if something goes wrong,
        otherwise is True untill user quit\n
        note: before updating call \"load_assets\" before main game loop
        """
        try:
            self.blit_assets()
        except AttributeError as e:
            print(f"> AttributeError: {e}")
            print(f"> assets are not loaded properly\n> call load_assets before game loop")
            return False

        try:
            self.update_objects(key)
        except Exception as e:
            print(f"{e}")
            print(f"> groups are not created yet\n> call create_objects")
            return False
        
        
        
        self.wave_control()
        self.check_powerup_collision()
        if self.shield: # immune to any damage from aliens
            self.collision_checks()
        else:
            self.collision_danger_check()
            self.collision_checks()
        self.game_over = self.ui.update()
        pygame.display.update()
        

        if self.game_pause:
            return self.pause()
        if self.game_over:
            soundGameOver.play()
            return self.over()
#        if self.player_score == 15000:
#            return self.won()
        if self.game_finished:
            return False



        return True
