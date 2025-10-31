from settings import *
from aliens import UnitGreenGenerator
from aliens import UnitRedGenerator
from aliens import UnitCyanGenerator

class Waves():
    def __init__(self,screen):
        super().__init__()
        self.display_surface = screen
        self.units_green = UnitGreenGenerator(screen = self.display_surface)
        self.units_red = UnitRedGenerator(screen = self.display_surface)
        self.units_cyan = UnitCyanGenerator(screen = self.display_surface)
        
        self.units_two_green = UnitGreenGenerator(screen = self.display_surface)
        self.units_two_red = UnitRedGenerator(screen = self.display_surface)
        self.units_two_cyan = UnitCyanGenerator(screen = self.display_surface)
        
        self.wave_done = 0
        self.cooldown_wave = 3000
        self.ongoing = True
        
        # TODO later
        self.boss_fight = None

    def wave_first(self):  
        if self.ongoing:
            self.ongoing = self.units_green.update()

        if not self.ongoing: # False
            if self.cooldown_wave >= 0:
                self.cooldown_wave -= 10
        
        if not self.ongoing and self.cooldown_wave <= 0:
            self.cooldown_wave = 3000
            return True

            
            
    def wave_second(self,prev_done):
        self.ongoing = prev_done
        if prev_done:
            self.ongoing = self.units_red.update()
                  
        if not self.ongoing: # False
            if self.cooldown_wave >= 0:
                self.cooldown_wave -= 10
        
        if not self.ongoing and self.cooldown_wave <= 0:
            self.cooldown_wave = 3000
            return True

    
    def wave_third(self,prev_done):
        self.ongoing = prev_done
        if prev_done:
            self.ongoing = self.units_cyan.update()
            
        if not self.ongoing: # False
            if self.cooldown_wave >= 0:
                self.cooldown_wave -= 10
        
        if not self.ongoing and self.cooldown_wave <= 0:
            self.cooldown_wave = 3000
            return True

        
    def wave_fourth(self,prev_done):
        if prev_done:
            self.ongoing = self.units_two_green.update()
            self.units_two_red.update()
            self.units_two_cyan.update()
        
        if not self.ongoing: # False
            if self.cooldown_wave >= 0:
                self.cooldown_wave -= 10
        
        if not self.ongoing and self.cooldown_wave <= 0:
            self.cooldown_wave = 3000
            return True


        



if __name__ == "__main__":
    pygame.init()
    test_surface = pygame.display.set_mode(SC_SIZE)
    pygame.display.set_caption("Test Guide Man")
    clock = pygame.Clock()

    # group
    waves = Waves(test_surface)
        
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_q):
                break
        test_surface.fill((30,30,30))       
        
        #group.update\
        # waves.wave_second()
        waves.wave_fourth()
            
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
