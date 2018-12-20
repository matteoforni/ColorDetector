#author matteoforni
#date: 19.12.2018
#Program that print the RGB color of the pixel under the mouse cursor.

import pygame
import sys
import os
from tkinter import *
from tkinter import filedialog

root = Tk()
img =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
pygame.init()
os.system('cls')
surface = pygame.display.set_mode( (500, 500) )
last_color = None

try:
    title = "Color detector: " + img
    pygame.display.set_caption(title)
    img = pygame.image.load(img)
except pygame.error:
    print('Cannot load image:', img)
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
