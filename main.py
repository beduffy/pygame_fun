import time
import sys
# from math import dist
import numpy as np
import random

import pygame


pygame.init()

width, height = 1000, 500
size = (width, height)

scalar_speed = 1
scalar_speed = 5
speed = [scalar_speed, scalar_speed]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

ballrect.center = (300, 100)

def dist_np(a, b):
    a = np.array(a)
    b = np.array(b)
    dist = np.sqrt(np.sum(np.square(a-b)))
    return dist

moving = False
frame_count = 0
# game main loop
while True:
    # user input
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            print('0 key pressed')
        if event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()

            dist_ball_to_mouse_click = dist_np(ballrect.center, click_pos)
            print('dist_ball_to_mouse_click:', dist_ball_to_mouse_click)

            if dist_ball_to_mouse_click < 50:
                moving = not moving
                if moving:
                    speed = [scalar_speed, scalar_speed]
                else:
                    speed = [0, 0]
                

    # mouse_x, mouse_y = pygame.mouse.get_pos()
    # print('Mouse:', mouse_x, mouse_y)
    # ball perfectly follows mouse
    # ballrect.center = mouse_x, mouse_y

    # dist_ball_to_mouse = dist_np(ballrect.center, (mouse_x, mouse_y))
    # print('dist_ball_to_mouse:', dist_ball_to_mouse)

    # TODO: make the ball avoid the mouse
    # super simple but lame: just be a certain radius away
    # complex: hardcore velocity based AI trying to escape from mouse

    # TODO: ball moves around. If you click it, it stops. If you click again it moves again
    

    # update physics
    # if dist_ball_to_mouse < 50:
    #     speed[0] = 1

    #     # # if ball goes to edge of left or right side of screen, we will invert x-velocity
    #     # if ballrect.left < 0 or ballrect.right > width:
    #     #     # speed[0] = -speed[0]
    #     #     ballrect.center = (100, 200)
    #     #     print('inverting')
    #     # # if ball goes the top or bottom side of screen, we will invert y-velocity
    #     # if ballrect.top < 0 or ballrect.bottom > height:
    #     #     speed[1] = -speed[1]
    # else:
    #     speed[0] = 0

    
    
    ballrect = ballrect.move(speed)

    # if ball goes to edge of left or right side of screen, we will invert x-velocity
    if ballrect.left < 0 or ballrect.right > width:
        # speed[0] = -speed[0]
        # speed[0] = -speed[0] * random.randint(1, 5)
        speed[0] = random.randint(-5, 5)
    # if ball goes the top or bottom side of screen, we will invert y-velocity
    if ballrect.top < 0 or ballrect.bottom > height:
        # speed[1] = -speed[1]
        # speed[1] = -speed[1] * random.randint(1, 5)
        speed[1] = random.randint(-5, 5)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(0.001)
    frame_count = frame_count + 1