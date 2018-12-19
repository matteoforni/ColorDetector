import pygame
import sys
import os

pygame.init()
os.system('cls')
surface = pygame.display.set_mode( (500, 500) )
last_color = None
if len(sys.argv) == 2:
    img = pygame.image.load(sys.argv[1])
else:
    print("Inserisci un immagine")
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
