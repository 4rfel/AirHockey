from subprocess import call
from os import environ
from ClassDisk import Disk
from ClassStricker import Stricker
import mss
import numpy as np
import cv2

from opencvDefs import getCircleCenter
pip3 = True
if pip3:
    try:
        import mss
    except ImportError:
        call(['pip3', 'install', "MSS"])
    finally:
        import mss

    try:
        import cv2
    except ImportError:
        call(['pip3', 'install', "python-opencv==3.4.2.17"])
    finally:
        import cv2

    try:
        import clock
    except ImportError:
        call(['pip3', 'install', "clock"])
    finally:
        import clock

    try:
        import pygame
    except ImportError:
        call(['pip3', 'install', "pygame"])
    finally:
        import pygame

else:

    try:
        import mss
    except ImportError:
        call(['pip', 'install', "MSS"])
    finally:
        import mss

    try:
        import cv2
    except ImportError:
        call(['pip', 'install', "python-opencv==3.4.2.17"])
    finally:
        import cv2

    try:
        import clock
    except ImportError:
        call(['pip', 'install', "clock"])
    finally:
        import clock

    try:
        import pygame
    except ImportError:
        call(['pip', 'install', "pygame"])
    finally:
        import pygame

black = [0,0,0]

pygame.init()

environ['SDL_VIDEO'] = '1'

clock = pygame.time.Clock()

display_specs = pygame.display.Info()

width_screen = int(display_specs.current_w/2)
height_screen = display_specs.current_h + 23

screen = pygame.display.set_mode((width_screen,height_screen))

FPS = 500

disk = Disk("disk.png")
cpuStricker = Stricker("stricker.png", (500,800))

sprites_group = pygame.sprite.Group()
sprites_group.add(cpuStricker)
sprites_group.add(disk)

lowerGreen = (55,   0,   0)
upperGreen = (65, 255, 255)

lowerPink = (int(295/2)-5,   0,   0)
upperPink = (int(295/2)+5, 255, 255)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == pygame.QUIT :
               running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    with mss.mss() as sct:
        monitor = {'top': 40, 'left': 120, 'width': int(width_screen-120), 'height': height_screen-100}
        img = np.array(sct.grab(monitor))

    diskCenter = getCircleCenter(img, lowerGreen, upperGreen)
    cpuStrickerCenter = getCircleCenter(img, lowerPink, upperPink)
    
    cv2.imshow('OpenCv Window', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        running = False
        break

    disk.move()
    cpuStricker.move(diskCenter, cpuStrickerCenter)
    sprites_group.draw(screen)
    pygame.display.update()
    screen.fill(black)