from subprocess import call
from os import environ
from ClassDisk import Disk
from ClassStricker import StrickerCPU, StrickerPlayer
import mss
import numpy as np
import cv2

from opencvDefs import *

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

clock = pygame.time.Clock()

screen_width = 700
screen_height = 980

screen = pygame.display.set_mode((screen_width ,screen_height))

FPS = 60

disk = Disk("disk.png", screen_width, screen_height)
cpuStricker = StrickerCPU("strickerCPU.png", (screen_width/2,700))
playerStricker = StrickerPlayer("strickerPlayer.png")


sprites_group = pygame.sprite.Group()
sprites_group.add(cpuStricker)
sprites_group.add(playerStricker)
sprites_group.add(disk)

lowerGreen = (55,   0,   0)
upperGreen = (65, 255, 255)

lowerPink = (int(295/2)-5,   0,   0)
upperPink = (int(295/2)+5, 255, 255)

y_horizontal_line = 600

running = True

previous_center = None
diskCenter = None
first_pass = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == pygame.QUIT :
               running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    with mss.mss() as sct:
        monitor = {'top': 60, 'left': 120, 'width': int(screen_width), 'height': screen_height}
        img = np.array(sct.grab(monitor))
        draw_action_line(img, y_horizontal_line)

    previous_center = diskCenter
    diskCenter = get_circle_center(img, lowerGreen, upperGreen)
    cpuStrickerCenter = get_circle_center(img, lowerPink, upperPink)
    if not first_pass:
        line2 = draw_path_prediction(img, previous_center, diskCenter)
        line11 = (0           ,y_horizontal_line)
        line12 = (screen_width, y_horizontal_line)
        intercection_point = line_intersection(img, (line11, line12), line2)
    else:
        first_pass = False

    cv2.imshow('OpenCv Window', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        running = False
        break

    disk.move(screen_width, screen_height)
    playerStricker.move()
    # cpuStricker.move(diskCenter, cpuStrickerCenter)
    sprites_group.draw(screen)
    pygame.display.update()
    screen.fill(black)