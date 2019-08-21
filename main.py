from subprocess import call
from os import environ
from ClassDisk import Disk

try:
    import pygame
except ImportError:
    call(['pip3', 'install', name])
finally:
    import pygame


# import ClassDisk


pygame.init()

environ['SDL_VIDEO_CENTERED'] = '1'

display_specs = pygame.display.Info()

width_screen = display_specs.current_w
height_screen = display_specs.current_h + 23

FPS = 90

disk = Disk("disk.png")

sprites_group = pygame.sprite.Group()
sprites_group.add(disk)



