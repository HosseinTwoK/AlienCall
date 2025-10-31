from settings import *

class ComingSoon(): # Hmmmm! i don't feel code it yet since i'm not familiar enough with deep concepts
    """to show start screen before starting the gameplay"""
    def __init__(self,screen:pygame.Surface):
        self.display_surface = screen    
        self.fontLarge = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),50)
        self.fontSmall = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),22)
        
        self.image = pygame.image.load(path.join("assets","sprites","boss","boss.png"))
        self.rect = self.image.get_rect()
        
    def texts_load(self):
        self.text_title = self.fontLarge.render("404 BOSS NOT FOUND", True, CLR_DBLUE)
        self.rect_title = self.text_title.get_rect()
        self.rect_title.center = POS_CENTER
        self.rect_title.y -= 20
         
        self.text_q = self.fontSmall.render("Press \"Q\" to quit", True, CLR_DBLUE)
        self.rect_q = self.text_q.get_rect()
        self.rect_q.center = POS_CENTER
        self.rect_q.y +=40
         
    def texts_blit(self):
        self.display_surface.fill(CLR_WHITE)
        self.texts_load()
        
        self.rect.center = POS_CENTER
        self.rect.y -= 120
        
        self.display_surface.blit(self.image, self.rect)  
        self.display_surface.blit(self.text_title, self.rect_title)
        self.display_surface.blit(self.text_q, self.rect_q)    
        pygame.display.update()
        
    def show_end(self):
        """starts screen loop
        \nreturn:
        True to start game, 
        False to quit"""

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    running = False
                
            self.texts_blit()
            
            
            

if __name__ == "__main__":
    pygame.init()
    
    test_surface = pygame.display.set_mode(SC_SIZE)
    pygame.display.set_caption("Test BOSS Screen")
    tst = ComingSoon(test_surface)
    result = tst.show_start()
    
    pygame.quit()
    
