# Import required libraries
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((640, 480))

# Load the robot image
robot = pygame.image.load("robot.png")

# Set up initial velocities for movement
y_velocity = 1
x_velocity = 1

# Set up the game clock
clock = pygame.time.Clock()

# Define the number of robots
numbers = 20

# Initialize a list to store robot positions
robots = []

# Generate initial random positions for each robot and add them to the list
for i in range(numbers):
    x = random.randint(0, 640 - robot.get_width())  # Random start position on the x-axis
    y = random.randint(-1000, 0)  # Each robot starts at a different position, outside the window
    robots.append([x, y])  # Add the new random start position to the list

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Update positions of each robot
    for i in range(numbers):
        # Move the robot downward if it's not at the bottom of the window
        if robots[i][1] + robot.get_height() < 480:
            robots[i][1] += y_velocity

        # Check if the robot has reached the bottom or top of the window
        if robots[i][1] + robot.get_height() == 480 or robots[i][1] <= 0 - robot.get_height():
            # If the robot is on the right side, move it to the right
            if robots[i][0] >= 640 // 2:
                robots[i][0] += x_velocity
                # If the robot goes out of the screen on the right, reset its position
                if robots[i][0] >= 640:
                    robots[i][0] = random.randint(0, 640 - robot.get_width())
                    robots[i][1] = random.randint(-1000, -100)
            # If the robot is on the left side, move it to the left
            else:
                robots[i][0] -= x_velocity
                # If the robot goes out of the screen on the left, reset its position
                if robots[i][0] <= 0:
                    robots[i][0] = random.randint(0, 640 - robot.get_width())
                    robots[i][1] = random.randint(-1000, -100)

    # Fill the window with a black background
    window.fill((0, 0, 0))

    # Draw each robot at its current position
    for i in range(numbers):
        window.blit(robot, (robots[i][0], robots[i][1]))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)
