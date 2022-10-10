import time
import sys
# from math import dist
import numpy as np
import random
import math

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

# spacing = 111
# all_balls = []
# for y in range(10):
#     for x in range(10):
#         ballrect = ball.get_rect()
#         ballrect.center = (x * spacing, y * spacing)
#         all_balls.append(ballrect)

centre_of_screen = int(round(width / 2)), int(round(height / 2))
ballrect = ball.get_rect()


def dist_np(a, b):
    a = np.array(a)
    b = np.array(b)
    dist = np.sqrt(np.sum(np.square(a-b)))
    return dist

angle = 0
radius_of_orbit = 150
moving = False
frame_count = 0
# game main loop
while True:
    # user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            print('0 key pressed')
        if event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()

    mouse_x, mouse_y = pygame.mouse.get_pos()

    ballcenter = (mouse_x - radius_of_orbit * math.sin(angle), mouse_y - radius_of_orbit * math.cos(angle))
    ballrect.center = ballcenter

    angle += 0.01
    # radius_of_orbit += 0.1
    # radius_of_orbit = random.randint(20, 200)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(0.001)
    frame_count = frame_count + 1