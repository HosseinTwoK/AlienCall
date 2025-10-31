from settings import *


class UI():
    def __init__(self,screen:pygame.Surface, lives):
        self.display_surface = screen
        self.top_HUD = (SC_WIDTH, 40)
        self.player_lives = lives
        
        self.lives = []
        for i in range(self.player_lives):
            heart = pygame.image.load(path.join("assets", "sprites", "powerup","heart.png"))
            self.lives.append(heart)

        self.heart_px = 20
        
        self.fontLarge = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),50)
        self.fontMedium = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),24)
        self.fontSmall = pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),18)
                
        self.player_score = 0
        self.wave_number = 1
        
        
        
    def add_life(self):
        if len(self.lives) < PLAYER_MAX_LIVES:
            self.lives.append(pygame.image.load(path.join("assets", "sprites", "powerup","heart.png")))
            self.player_lives += 1
        else:
            print("healt is full")
        
        return self.player_lives


    def remove_life(self):
        if len(self.lives) > 0:
            self.lives.pop(len(self.lives)-1)
            self.player_lives -= 1            
        else:
            print("you are dead") 
            
        return self.player_lives
    
    
    def add_score(self,score):
        self.player_score += score
    
    
    def update_wave(self,w):
        self.wave_number = w
    
    
    def update(self):
        pygame.draw.rect(self.display_surface,CLR_WHITE,((0,0),self.top_HUD))

        if self.lives != []:  
            for i,heart in enumerate(self.lives):
                rect = heart.get_rect()
                rect.topright = (SC_WIDTH - 10 - i*self.heart_px , 10)
                self.display_surface.blit(heart, rect)
        else:
            return True # game over
        
        text_score = self.fontSmall.render(f"Wave: {self.wave_number}", True, CLR_DBLUE)
        rect_score = text_score.get_rect()
        rect_score.topleft = ( 350 , 10)
        self.display_surface.blit(text_score, rect_score)
        
        text_score = self.fontSmall.render(f"Score: {self.player_score}", True, CLR_DBLUE)
        rect_score = text_score.get_rect()
        rect_score.topleft = ( 10 , 10)
        self.display_surface.blit(text_score, rect_score)
        
        return False
        

if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode(SC_SIZE)
    pygame.display.set_caption("UI TEST")
    clock = pygame.time.Clock()
    
    ui = UI(screen,5)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                break
        
        ui.update()
        pygame.display.update() 
        clock.tick(60)