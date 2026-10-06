import pygame
from sys import exit

#WINDOW VARIABLES/CONSTANTS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) #creates window
pygame.display.set_caption("Spotify pal")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
