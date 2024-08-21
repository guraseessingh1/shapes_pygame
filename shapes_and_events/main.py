import pygame

pygame.init()



screen = pygame.display.set_mode([500,500])
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)

#filling background colour of the screen
screen.fill(white)

#creating circle class
class Circle():
    def __init__(self,pos,radius,width=0):



