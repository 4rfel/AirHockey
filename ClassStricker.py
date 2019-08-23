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



class StrickerCPU(Stricker):
    def __init__(self, img, startPosition):
        Stricker.__init__(self, img, startPosition)
        self.screen_center = startPosition

    def move(self, diskCenter, strickerCenter):
        if diskCenter != None and strickerCenter != None and self.rect.left > 0:
            diskX = diskCenter[0]
            diskY = diskCenter[1]

            strickerX = strickerCenter[0]
            strickerY = strickerCenter[1]
            # print(self.rect.left, self.rect.right, "\n")
            # if self.rect.right < self.screen_center[0]:
            if   strickerX > diskX-50:
                self.rect.centerx -= self.xspeed
            elif strickerX < diskX+50:
                self.rect.centerx += self.xspeed
        elif self.rect.left > 0:
            self.rect.centerx -= self.xspeed
        elif self.rect.right < 600:
            self.rect.centerx += self.xspeed


        
        
        
        


class StrickerPlayer(Stricker):
    def __init__(self, img):
        mousePosition = pygame.mouse.get_pos()
        Stricker.__init__(self, img, (0,0))

    def move(self):
        if self.rect.bottom < 400:
            self.rect.center = pygame.mouse.get_pos()
        if pygame.mouse.get_pos()[1] < 400:
            self.rect.center = pygame.mouse.get_pos()
            # print(pygame.mouse.get_pos())
        else:
            self.rect.centerx = pygame.mouse.get_pos()[0]

