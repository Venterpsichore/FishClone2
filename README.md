# FishClone2

My intention is to practice Python as I create a RPG centered around sea monsters. I would like to work on this more to create more area to travel, a motley of aquatic species, and dialogue to incorporate decision-making, choices, and voice.
I would like to work with others on games as well as they pertain to horror, role-playing, fantasy, mystery, and sci-fi.

*************************************************************************************************
Adding the movement of a ball to simulate player avatar movement and background correspondent to different keys, simulating a plot point or dialogue change. 

'''
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

key_dict = {K_s:darkseagreen2, K_c:chocolate1, K_k:cornsilk2, 
    K_o:mediumorchid2, K_e:orangered1, K_b:slateblue1, K_p:plum,
    K_l:olivedrab1, K_t:thistle2, K_g:magenta2, K_i:midnightblue,
    K_d:darkorange3, K_n:mediumspringgreen, K_y:slategray1}
    '''

'''
all = pygame.image.load("Rugged_ball.jpg")
rect = ball.get_rect()
speed = [2, 2]
'''

'''
running = True
background = grey99
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict [event.key]

                caption = 'background color is newly ' + str(background)
                pygame.display.set_caption(caption)
'''

To contribute or for any questions, feel free to message me at the following links.

LinkedIn: www.linkedin.com/in/jasevillarreal
Email: charybdiskylla@gmail.com
