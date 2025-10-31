from settings import *
from game import Game
from startscreen import Start
from guideman import IntroGuide

pygame.init()

display_surface = pygame.display.set_mode(SC_SIZE)
icon = pygame.image.load(path.join("assets","sprites","player.png")).convert_alpha()
pygame.display.set_caption("Alien Call")
pygame.display.set_icon(icon)

#pygame.mixer.music.load(path.join("assets","sounds","bgmusic.wav"))
#pygame.mixer.music.set_volume(0.3)

clock = pygame.time.Clock()
start = Start(screen = display_surface)
game = Game(screen = display_surface)
guide_man = IntroGuide(screen = display_surface)

game.load_assets() 
game.create_groups()

guide_shown = False
bgmusic_play = False

running = start.show_start()
soundGuideManLoad.play()
while running:
    key = ""
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                key = "SPACE"
            if event.key == K_ESCAPE:
                key = "ESC"

    running = game.update(key)

#    if guide_shown and not bgmusic_play:
#        pygame.mixer.music.play(-1,0.0)
#        bgmusic_play = True
    if not guide_shown:
        guide_shown = True
        running = guide_man.show_guide()
    
    
    clock.tick(FPS)


pygame.quit()
