# WRITE YOUR SOLUTION HERE:
import pygame
import math
import time

pygame.init()
display = pygame.display.set_mode((640, 480))

radius = 200
center = (320, 240)

num_points_sm = 60  # Number of points to divide the circle into (seconds, minutes)
num_points_h = 24  # Number of points to divide the circle into (hours)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))

    # Outer circle - black circle on top of a bigger red circle
    pygame.draw.circle(display, (255, 0, 0), center, 200)  # Outer red circle
    pygame.draw.circle(display, (0, 0, 0), center, 195)  # Inner black circle

    # Middle circle
    pygame.draw.circle(display, (255, 0, 0), center, 10)

    



    # Second line that changes position every second
    current_time = time.localtime()
    seconds = current_time.tm_sec
    t_s = (2 * math.pi * seconds) / num_points_sm
    x_s = center[0] + int(180 * math.cos(t_s))  # line shorter then the radius of the circle
    y_s = center[1] + int(180 * math.sin(t_s))
    pygame.draw.line(display, (0, 0, 255), center, (x_s, y_s), 1)  # seconds line

    # Minute line that changes position every minute
    current_time = time.localtime()
    minute = current_time.tm_min
    t_m = (2 * math.pi * minute) / num_points_sm
    x_m = center[0] + int(180 * math.cos(t_m))  
    y_m = center[1] + int(180 * math.sin(t_m))
    pygame.draw.line(display, (0, 0, 255), center, (x_m, y_m), 2)  # Minue line

    # Hour line that changes position every hour
    current_time = time.localtime()
    hour = current_time.tm_hour
    t_h = (2 * math.pi * hour) / num_points_h
    x_h = center[0] + int(120 * math.cos(t_h))  # Changing the radius to make the hour line smaller
    y_h = center[1] + int(120 * math.sin(t_h))
    pygame.draw.line(display, (0, 0, 255), center, (x_h, y_h), 4)  # Hour line






    pygame.display.flip()
