from settings import *


class IntroGuide():
    def __init__(self,screen):
        self.display_surface = screen
        self.messages_all = 9 # messages from guide-man in assets
        self.messages_current = 1
        
        
        self.next_isHovered = False
        self.prev_isHovered = False
        
        self.next_collided = False
        self.prev_collided = False
        
        self.finished = False
        self.show_next_text = False
        self.show_prev_text = False
    
        self.load_assets()


    def setup_overlay(self):
        """set overlay to show attention area in screen"""
        position = (0,0)
        size = (SC_SIZE)
        
        overlay = pygame.Surface(size)
        overlay.fill(CLR_WHITE)
        overlay.set_alpha(2)
        self.display_surface.blit(overlay,position)    
    
    
    def load_assets(self):
        fontMedium= pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),22)
        self.fontSmall= pygame.font.Font(path.join("assets","fonts","PixeloidSans.ttf"),16)
        
        self.text_start = fontMedium.render("PRESS \"SPACE\" TO ENTER THE SPACE SIR", True, CLR_DRED)
        self.rect_start = self.text_start.get_rect()
        self.rect_start.center = (POS_CENTER)
        self.rect_start.x += 160
        self.rect_start.y += 270
        
        
        self.text_next_ = self.fontSmall.render("Next: \"Enter\"", True, CLR_DBLUE)
        self.rect_next_ = self.text_next_.get_rect()
        self.rect_next_.x = 500
        self.rect_next_.y = 10
        
        
        self.text_prev_ = self.fontSmall.render("Previous: \"BackSpace\"", True, CLR_DBLUE)
        self.rect_prev_ = self.text_prev_.get_rect()
        self.rect_prev_.x = 200
        self.rect_prev_.y = 10
        
        self.messages = []
        for i in range(self.messages_all):
            self.messages.append(pygame.image.load(path.join("assets","sprites","guide-man",f"guide-person{i+1}.png")))

        self.message_image = self.messages[0]
        self.message_rect = self.message_image.get_rect()
        self.message_rect.topleft = (8,40)
        
        self.text_pagecount = self.fontSmall.render(f"{self.messages_current}/{self.messages_all}", True, CLR_DBLUE)
        self.rect_pagecount = self.text_pagecount.get_rect()
        self.rect_pagecount.x = 724
        self.rect_pagecount.y = 166  

        self.button_next_enabled = pygame.image.load(path.join("assets","sprites","guide-man","button-enabled.png"))
        self.button_next_hovered = pygame.image.load(path.join("assets","sprites","guide-man","button-hovered.png"))
        
        self.button_prev_enabled = pygame.image.load(path.join("assets","sprites","guide-man","button-enabled.png"))
        self.button_prev_hovered = pygame.image.load(path.join("assets","sprites","guide-man","button-hovered.png"))

        
        

    def set_buttons(self):
        """set buttons enable to click or disable to remove from screen"""
        # this method is required in button_update()
        if self.messages_current == 1:
            self.button_next = self.button_next_enabled
            self.button_prev = False
            self.show_next_text = True
            self.show_prev_text = False
        elif self.messages_current > 1 and self.messages_current < self.messages_all:
            self.button_next = self.button_next_enabled
            self.button_prev = self.button_prev_enabled
            self.show_next_text = True
            self.show_prev_text = True
        elif self.messages_current >= self.messages_all:
            self.button_next = False
            self.button_prev = self.button_prev_enabled
            self.show_next_text = False
            self.show_prev_text = True
            
            

    def go_next(self):
        if self.messages_current < self.messages_all and self.button_next:
            self.messages_current += 1
            self.message_image = self.messages[self.messages_current-1]
            self.pagecount_update()
            
   
    def go_prev(self):
        if self.messages_current >= 2 and self.button_prev:
            self.messages_current -= 1
            self.message_image = self.messages[self.messages_current-1]
            self.pagecount_update()
            
    
    def pagecount_update(self):
        self.text_pagecount = self.fontSmall.render(f"{self.messages_current}/{self.messages_all}", True, CLR_DBLUE)


    def button_update(self):
        """update button state"""
        # requires set_button() before processing
        self.set_buttons()
        
        if self.button_next:
            if self.next_isHovered:
                self.button_next = self.button_next_hovered

            # set position next button
            self.rect_button_next = self.button_next.get_rect()
            next_x , next_y = self.message_rect.bottomright
            self.rect_button_next.bottomright = (next_x-60,next_y-60)

            self.next_collided = True if self.rect_button_next.collidepoint(pygame.mouse.get_pos()) else False            
            if self.next_collided and self.button_next:
                self.next_isHovered = True
            else:
                self.next_isHovered = False
        
        
        if self.button_prev:
            if self.prev_isHovered:
                self.button_prev = self.button_prev_hovered

            # set button prev
            self.button_prev = pygame.transform.flip(self.button_prev,True,False)
            self.rect_button_prev = self.button_prev.get_rect()
            prev_x , prev_y = self.rect_button_next.bottomright
            self.rect_button_prev.bottomright = (prev_x-20,prev_y)
            
            self.prev_collided = True if self.rect_button_prev.collidepoint(pygame.mouse.get_pos()) else False  
            if self.prev_collided and self.button_prev:
                self.prev_isHovered = True
            else:
                self.prev_isHovered = False
                
            
        
        
    def blit_message(self):
        self.setup_overlay()
        self.display_surface.blit(self.message_image, self.message_rect)
        
        self.display_surface.blit(self.text_pagecount, self.rect_pagecount)
        
        if self.show_next_text:
            self.display_surface.blit(self.text_next_, self.rect_next_)
        if self.show_prev_text:
            self.display_surface.blit(self.text_prev_, self.rect_prev_)
        
        if self.button_next:
            self.display_surface.blit(self.button_next, self.rect_button_next)
        if self.button_prev:
            self.display_surface.blit(self.button_prev, self.rect_button_prev)
            
        if self.messages_current == self.messages_all:
            self.display_surface.blit(self.text_start,self.rect_start)
            self.finished = True
        else:
            self.finished = False
            
        
        
        pygame.display.update()
        

    def show_guide(self):
        """loop to show guides untill user see all guide messages
        return False if player wants to quit otherwise return True"""
        while self.messages_current <= self.messages_all:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.messages_all = 0
                    return False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.next_collided:
                        self.go_next()
                    if self.prev_collided:
                        self.go_prev()
                
                if event.type == KEYDOWN:
                    if event.key == K_BACKSPACE and self.button_prev:
                        self.go_prev()
                    if event.key == K_RETURN and self.button_next:
                        self.go_next()
                        
                    if event.key == K_SPACE and self.finished:
                        self.messages_all = 0
                        

                        
            self.button_update()
            self.blit_message()     
               
        return True
                    

                        
                    

            
            

if __name__ == "__main__":
    pygame.init()
    
    test_surface = pygame.display.set_mode(SC_SIZE)
    pygame.display.set_caption("Test Guide Man")
    tst = IntroGuide(test_surface)
    tst.show_guide()
   
    pygame.quit()