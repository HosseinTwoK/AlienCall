from settings import *


class Start():
    """to show start screen before starting the gameplay"""
    def __init__(self,screen:pygame.Surface):
        self.display_surface = screen
            
        self.fontLarge = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),50)
        self.fontMedium = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),30)
        self.fontSmall = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),22)
        
    def texts_load(self):
        self.text_title = self.fontLarge.render("Alien Call", True, CLR_DBLUE)
        self.rect_title = self.text_title.get_rect()
        self.rect_title.center = POS_CENTER
        self.rect_title.y -= 200 
        
        self.text_enter = self.fontMedium.render("Press \"Enter\" to Start", True, CLR_DBLUE)
        self.rect_enter = self.text_enter.get_rect()
        self.rect_enter.center = POS_CENTER
        self.rect_enter.y -= 100
        
        self.text_q = self.fontSmall.render("Press \"Q\" to quit", True, CLR_DBLUE)
        self.rect_q = self.text_q.get_rect()
        self.rect_q.center = POS_CENTER
        self.rect_q.y -= 40
        
        self.text_gamecontrol = self.fontMedium.render("- - - Game Control - - -", True, CLR_DBLUE)
        self.rect_gamecontrol = self.text_gamecontrol.get_rect()
        self.rect_gamecontrol.center = POS_CENTER
        self.rect_gamecontrol.y += 30
        
        # under --game control-- : left side
        self.text_toleft = self.fontSmall.render("A : move left", True, CLR_DBLUE)
        self.rect_toleft = self.text_toleft.get_rect()
        self.rect_toleft.topleft = POS_CENTER
        self.rect_toleft.y += 90
        self.rect_toleft.x -= 250
        
        self.text_toright = self.fontSmall.render("D: move right", True, CLR_DBLUE)
        self.rect_toright = self.text_toright.get_rect()
        self.rect_toright.topleft = POS_CENTER
        self.rect_toright.y += 130
        self.rect_toright.x -= 250
        
        self.text_toup = self.fontSmall.render("W : move up", True, CLR_DBLUE)
        self.rect_toup = self.text_toup.get_rect()
        self.rect_toup.topleft = POS_CENTER
        self.rect_toup.y += 170
        self.rect_toup.x -= 250
        
        self.text_todown = self.fontSmall.render("S : move down", True, CLR_DBLUE)
        self.rect_todown = self.text_todown.get_rect()
        self.rect_todown.topleft = POS_CENTER
        self.rect_todown.y += 210
        self.rect_todown.x -= 250

        # under --game control-- : right side
        self.text_topause = self.fontSmall.render("ESC : pause game", True, CLR_DBLUE)
        self.rect_topause = self.text_topause.get_rect()
        self.rect_topause.topleft = POS_CENTER
        self.rect_topause.y += 90
        self.rect_topause.x += 100
        
        self.text_toshoot = self.fontSmall.render("SPACE : shoot", True, CLR_DBLUE)
        self.rect_toshoot = self.text_toshoot.get_rect()
        self.rect_toshoot.topleft = POS_CENTER
        self.rect_toshoot.y += 130
        self.rect_toshoot.x += 100
        
    def texts_blit(self):
        self.display_surface.fill(CLR_WHITE)
        self.texts_load()
               
        self.display_surface.blit(self.text_title, self.rect_title)
        self.display_surface.blit(self.text_enter, self.rect_enter)
        self.display_surface.blit(self.text_q, self.rect_q)    
        self.display_surface.blit(self.text_gamecontrol, self.rect_gamecontrol)
        
        self.display_surface.blit(self.text_toleft, self.rect_toleft)
        self.display_surface.blit(self.text_toright, self.rect_toright)
        self.display_surface.blit(self.text_toup, self.rect_toup)
        self.display_surface.blit(self.text_todown, self.rect_todown)
        
        self.display_surface.blit(self.text_topause, self.rect_topause)
        self.display_surface.blit(self.text_toshoot, self.rect_toshoot)
        
        pygame.display.update()
        
    def show_start(self):
        """starts screen loop
        \nreturn:
        True to start game, 
        False to quit"""

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    return False
                if event.type == KEYDOWN and event.key == K_RETURN:
                    return True
            self.texts_blit()
            
            

if __name__ == "__main__":
    pygame.init()
    
    test_surface = pygame.display.set_mode(SC_SIZE)
    pygame.display.set_caption("Test Start Screen")
    tst = Start(test_surface)
    result = tst.show_start()
    print(result)
    
    pygame.quit()
    