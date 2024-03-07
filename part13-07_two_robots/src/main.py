import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x_1 = 0
y_1 = 50
velocity_1 = 1
x_2 = 0
y_2 = 150  # Separate initial y position for the second robot
velocity_2 = 2  # Double the speed of the first robot
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x_1, y_1))
    window.blit(robot, (x_2, y_2))
    pygame.display.flip()

    x_1 += velocity_1
    if velocity_1 > 0 and x_1 + robot.get_width() >= 640:
        velocity_1 = -velocity_1
    if velocity_1 < 0 and x_1 <= 0:
        velocity_1 = -velocity_1

    x_2 += velocity_2
    if velocity_2 > 0 and x_2 + robot.get_width() >= 640:
        velocity_2 = -velocity_2
    if velocity_2 < 0 and x_2 <= 0:
        velocity_2 = -velocity_2

    clock.tick(60)
