import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PlatformerGame")

bg_image = pygame.image.load('img/sky.png')
bg_image = pygame.transform.scale(bg_image, (800, 700))

run = True
while run:

    screen.blit(bg_image,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #display images
    pygame.display.update()

pygame.quit()