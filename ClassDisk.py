import pygame

class Disk(pygame.sprite.Sprite):
    def __init__(self, img, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width/2, screen_height/2)
        self.xspeed = 10
        self.yspeed = -10

    def move(self, screen_width, screen_height):
        # self.rect.center = pygame.mouse.get_pos()
        if self.rect.left > 0 and self.rect.right < screen_width:
            self.rect.centerx += self.xspeed
        else:
            self.xspeed = -self.xspeed
            self.rect.centerx += self.xspeed

        if self.rect.top > 0 and self.rect.bottom < 800:
            self.rect.centery += self.yspeed
        else:
            self.yspeed = -self.yspeed
            self.rect.centery += self.yspeed

    # def change_speed(self):
    #     self.xspeed = 5
