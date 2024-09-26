import pygame
from pygame.locals import *

chocolate1 = (255, 127, 36, 255)
cornsilk2 = (238, 232, 205, 255)
darkseagreen2 = (180, 238, 180, 255)
grey99 = (252, 252, 252, 255)
magenta2 = (238, 0, 238, 255)
mediumorchid2 = (209, 95, 238, 255)
mediumspringgreen = (0, 250, 154, 255)
midnightblue = (25, 25, 112, 255)
orangered1 = (255, 69, 0, 255)
olivedrab1 = (192, 255, 62, 255)
slategray1 = (198, 226, 255, 255)
slateblue1 = (131, 111, 255, 255)
plum = (221, 160, 221, 255)
thistle2 = (238, 210, 238, 255)
darkorange3 = (205, 102, 0, 255)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 240))


running = True
background = grey99
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                background = darkseagreen2
            elif event.key == pygame.K_c:
                background = chocolate1
            elif event.key == pygame.K_k:
                background = cornsilk2
            elif event.key == pygame.K_o:
                background = mediumorchid2
            elif event.key == pygame.K_e:
                background = orangered1
            elif event.key == pygame.K_b:
                background = slateblue1
            elif event.key == pygame.K_p:
                background = plum
            elif event.key == pygame.K_l:
                background = olivedrab1
            elif event.key == pygame.K_t:
                background = thistle2
            elif event.key == pygame.K_g:
                background = magenta2
            elif event.key == pygame.K_i:
                background = midnightblue
            elif event.key == pygame.K_d:
                background = darkorange3
            elif event.key == pygame.K_n:
                background = mediumspringgreen
            elif event.key == pygame.K_y:
                background =slategray1

            
            

        print(event)


    screen.fill(background)
    pygame.display.update()            

pygame.quit()