from subprocess import call
from os import environ
from ClassDisk import Disk
import clock

try:
    import pygame
except ImportError:
    call(['pip3', 'install', "pygame"])
finally:
    import pygame

black = [0,0,0]

pygame.init()

environ['SDL_VIDEO_CENTERED'] = '1'

clock = pygame.time.Clock()

display_specs = pygame.display.Info()

width_screen = display_specs.current_w
height_screen = display_specs.current_h + 23

screen = pygame.display.set_mode((width_screen,height_screen))

FPS = 120

disk = Disk("disk.png")

sprites_group = pygame.sprite.Group()
sprites_group.add(disk)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == pygame.QUIT :
               running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    disk.move()
    sprites_group.draw(screen)
    pygame.display.update()
    screen.fill(black)




    
