#author matteoforni
#date: 19.12.2018
#Program that print the RGB color of the pixel under the mouse cursor.

import pygame
import sys
import os
import time

pygame.init()
os.system('cls')
surface = pygame.display.set_mode( (500, 500) )
last_color = None

if len(sys.argv) > 1:
    try:
        img = pygame.image.load(sys.argv[1])
    except pygame.error:
        print('Cannot load image:', sys.argv[1])
        exit()
else:
    print("Insert an image")
    exit()
surface.blit(img,(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    color = surface.get_at(pygame.mouse.get_pos())
    if last_color != color:
        print(color)
        last_color = color

    pygame.display.update()
pygame.quit()
