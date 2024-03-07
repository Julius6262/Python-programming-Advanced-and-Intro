# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0,0,0))
width = robot.get_width()
height = robot.get_height()

loop_width = 100-(width-10)  # Start width
loop_height = 200-height  # Start Height

for num in range(1,101):
    window.blit(robot, (loop_width, loop_height))

    loop_width += (width-10)
    
    if num % 10 == 0:  # Get a new row
        loop_height += (height/4) -1
        loop_width -= ((width-10)*10) -10

    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
