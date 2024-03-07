# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 0
y = 0
y_velocity = 2
x_velocity = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    x += x_velocity
    y += y_velocity

    if x + ball.get_width() >= 640 or x <= 0:
        x_velocity = -x_velocity

    if y + ball.get_height() >= 480 or y <= 0:
        y_velocity = -y_velocity

    clock.tick(60)