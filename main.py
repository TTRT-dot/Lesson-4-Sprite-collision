import pygame
import random

#constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500
MOVEMENT_SPEED = 5
FONT_SIZE = 72

#NITALIZE PYGAME
pygame.init()

background_img = pygame.transform.scale(pygame.image.load(),
                                        SCREEN_HEIGHT,SCREEN_WIDTH)
font=pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.color('dodgerblue'))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()

    def move(self,x_change,y_change):
        self.rect.x=max(
        min(self.rect.x+x.change,SCREEN_WIDTH - self.rect.width),0)
        self.rect.y=max(
        min(self.rect.y+y.change,SCREEN_HEIGHT - self.rect.height),0)

#setup
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites=pygame.sprite.group()

#Create sprite1
sprite1=Sprite(pygame.color('black'),20,30)
sprite1.rect.x,sprite1.rect.y=random.randint(
    0, SCREEN_WIDTH - sprite1.rect.width),random.randint(
        0,SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites=pygame.sprite.group()

#Create sprites2
sprite2=Sprite(pygame.color('black'),20,30)
sprite2.rect.x,sprite2.rect.y=random.randint(
    0, SCREEN_WIDTH - sprite2.rect.width),random.randint(
        0,SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

#game loop