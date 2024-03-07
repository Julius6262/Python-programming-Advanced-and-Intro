# WRITE YOUR SOLUTION HERE:

import pygame
import random
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 

x = 50
y = 50
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse = event.pos[0]  # 
            y_mouse = event.pos[1]

            left_x = x  # Left side position
            right_x = x + robot.get_width()  # Right side position

            upper_y = y  # Upper y-coordinate
            lower_y = y + robot.get_height()  # Lower y-coordinate

            if x_mouse > left_x and x_mouse < right_x:
                if y_mouse > upper_y and y_mouse < lower_y:
                    x = random.randint(0, 640 - robot.get_width())
                    y = random.randint(0, 480 - robot.get_height())
        
        screen.fill((0, 0, 0))
        screen.blit(robot, (x, y))
        pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()
