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
        self.start_position = startPosition
        self.in_home = False

    def move(self, strickerCenter, destination_predict):
        if strickerCenter is not None:
            if not self.in_home:
                # self.go_home(strickerCenter)
                self.in_home = True
            elif destination_predict != (-1,-1):
                self.in_home = False
                self.go_defend(strickerCenter, destination_predict)
            
    
    def go_home(self, strickerCenter):
        stricker_x = strickerCenter[0]
        stricker_y = strickerCenter[1]
        inY = inX = False
        
        if stricker_x < self.start_position[0]+5:
            self.rect.centerx += self.xspeed
        if stricker_x > self.start_position[0]-5:
            self.rect.centerx -= self.xspeed
        else:
            inX = True

        if stricker_y < self.start_position[1]+5:
            self.rect.centery += self.yspeed
        if stricker_y > self.start_position[1]-5:
            self.rect.centery -= self.yspeed
        else:
            inY = True

        if inX and inY:
            self.in_home = True
        
    def go_defend(self, strickerCenter, destination_predict):
        destination_x = destination_predict[0]
        destination_y = destination_predict[1]

        stricker_x = strickerCenter[0]
        stricker_y = strickerCenter[1]
        
        if stricker_x < destination_x+5:
            self.rect.centerx += self.xspeed
        if stricker_x > destination_x-5:
            self.rect.centerx -= self.xspeed

        if stricker_y < destination_y+5:
            self.rect.centery += self.yspeed
        if stricker_y > destination_y-5:
            self.rect.centery -= self.yspeed


class StrickerPlayer(Stricker):
    def __init__(self, img):
        mousePosition = pygame.mouse.get_pos()
        Stricker.__init__(self, img, (0,0))

    def move(self):
        if self.rect.bottom < 400:
            self.rect.center = pygame.mouse.get_pos()
        if pygame.mouse.get_pos()[1] < 400:
            self.rect.center = pygame.mouse.get_pos()
        else:
            self.rect.centerx = pygame.mouse.get_pos()[0]

