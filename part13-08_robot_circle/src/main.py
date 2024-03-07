import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

num_robots = 10
angles = [i * (2 * math.pi / num_robots) for i in range(num_robots)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))

    for i in range(num_robots):
        x = 320 + math.cos(angles[i]) * 100 - robot.get_width() / 2
        y = 240 + math.sin(angles[i]) * 100 - robot.get_height() / 2

        window.blit(robot, (x, y))
        angles[i] += 0.01

    
    pygame.display.flip()
    clock.tick(60)
