import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width, height = robot.get_size()  # Get dimensions of the robot image

screen.fill((0, 0, 0))

for i in range(1000):
    x = random.randint(0, 640 - width)
    y = random.randint(0, 480 - height)
    screen.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


