import pygame
from os import path


pygame.init()
# done
soundGuideManLoad = pygame.mixer.Sound(path.join("assets","sounds","menu-load.wav"))
soundGuideManLoad.set_volume(0.2)

soundGameOver = pygame.mixer.Sound(path.join("assets","sounds","game-over.wav"))
soundGameOver.set_volume(0.1)

# done
soundPlayerShoot = pygame.mixer.Sound(path.join("assets","sounds","player-shoot.wav"))
soundPlayerShoot.set_volume(0.1)

# done
soundPlayerDamaged = pygame.mixer.Sound(path.join("assets","sounds","player-damaged.wav"))
soundPlayerDamaged.set_volume(0.1)

# done
soundPowerUp = pygame.mixer.Sound(path.join("assets","sounds","powerup.wav"))
soundPowerUp.set_volume(0.1)

# done
soundAlienShoot = pygame.mixer.Sound(path.join("assets","sounds","alien-shoot.wav"))
soundAlienShoot.set_volume(0.1)

pygame.quit()