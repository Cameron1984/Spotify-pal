import pygame
from sys import exit

#WINDOW VARIABLES/CONSTANTS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480
CENTER = (400, 240)
BLACK = (0,0,0)

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) #creates window
pygame.display.set_caption("Spotify pal")
image = pygame.image.load('tna.png')
image = pygame.transform.scale(image, (400, 400))
w = image.get_width()
h = image.get_height()


def make_circle(image):
    #pick smallest side and set as size to make square
    size = min(image.get_width(), image.get_height())
    mask = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.circle(mask, (255, 255, 255, 255), (size // 2, size // 2), size // 2)
    
    # Create a copy of the original image cropped to a square area
    cropped_image = pygame.Surface((size, size), pygame.SRCALPHA)
    cropped_image.blit(image, (0, 0), (0, 0, size, size))
    
    # Blend the white circle mask with the cropped image 
    # BLEND_RGBA_MIN takes the lowest alpha value between the mask and the image
    mask.blit(cropped_image, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    
    return mask
#img2 = pygame.transform.scale(image, (w, h))

spin = 0

image = make_circle(image)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.fill(BLACK)
    img2 = pygame.transform.rotate(image, spin)
    img2_rect = img2.get_rect(center=CENTER)
    window.blit(img2, img2_rect)
    pygame.draw.circle(window,BLACK,(400, 240),20)

    pygame.display.update()
    spin+=2
    clock.tick(30) 




