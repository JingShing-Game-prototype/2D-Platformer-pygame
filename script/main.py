import pygame, sys
from settings import *
from level import Level

# pygame setup
pygame.init()
clock = pygame.time.Clock()
level = Level(level_data=level_map, surface=screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                crt_shader.change_shader()

    screen.fill('black')
    level.run()
    
    crt_shader()
    clock.tick(60)