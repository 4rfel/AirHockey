import pygame

class Stricker(pygame.sprite.Sprite):
    def __init__(self, img, startPosition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = startPosition
        self.xspeed = 20
        self.yspeed = 20

    def move(self, diskCenter, strickerCenter):
        diskX = diskCenter[0]
        diskY = diskCenter[1]

        strickerX = strickerCenter[0]
        strickerY = strickerCenter[1]

        if strickerX > diskX-21:
            self.rect.centerx-= self.xspeed
        elif strickerX < diskX+21:
            self.rect.centerx += self.xspeed

        # if self.rect.centery >= 600:

