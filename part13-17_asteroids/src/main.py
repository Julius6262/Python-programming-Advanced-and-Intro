import pygame
import random

class Robot:
    def __init__(self, image_path, initial_x, initial_y):
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = initial_x
        self.y = initial_y

class Rock:
    def __init__(self, image_path, initial_x, initial_y):
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = initial_x
        self.y = initial_y

class Game:
    def __init__(self, window_width, window_height, robot, rocks_count):
        pygame.init()
        self.window = pygame.display.set_mode((window_width, window_height))
        self.robot = robot
        self.rocks = [Rock("rock.PNG", random.randint(0, window_width - robot.width), random.randint(-1500, 0)) for _ in range(rocks_count)]

        self.to_right = False
        self.to_left = False

        self.clock = pygame.time.Clock()
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False

    def update_robot_position(self):
        if self.to_right and self.robot.x < (640 - self.robot.width):
            self.robot.x += 2
        if self.to_left and self.robot.x > 0:
            self.robot.x -= 2

    def update_rocks_position(self):
        for i in range(len(self.rocks)):
            if self.rocks[i].y + self.rocks[i].height < 480:
                self.rocks[i].y += 1

            if self.rocks[i].y + self.rocks[i].height >= 480:
                self.robot.x = random.randint(0, 640 - self.robot.width)
                self.robot.y = 480 - self.robot.height
                self.score = 0

                for j in range(len(self.rocks)):
                    self.rocks[j].y = random.randint(-1500, -100)

            left_x_rock = self.rocks[i].x
            right_x_rock = self.rocks[i].x + self.rocks[i].width
            upper_y_rock = self.rocks[i].y
            lower_y_rock = self.rocks[i].y + self.rocks[i].height

            left_x_robot = self.robot.x
            right_x_robot = self.robot.x + self.robot.width
            upper_y_robot = self.robot.y
            lower_y_robot = self.robot.y + self.robot.height

            if (
                right_x_robot > left_x_rock
                and left_x_robot < right_x_rock
                and lower_y_robot > upper_y_rock
                and upper_y_robot < lower_y_rock
            ):
                self.score += 1
                self.rocks[i].y = random.randint(-1000, -100)

    def run(self):
        while True:
            self.handle_events()
            self.update_robot_position()
            self.update_rocks_position()

            self.window.fill((0, 0, 0))
            self.window.blit(self.robot.image, (self.robot.x, self.robot.y))
            self.display_score()

            for i in range(len(self.rocks)):
                self.window.blit(self.rocks[i].image, (self.rocks[i].x, self.rocks[i].y))

            pygame.display.flip()
            self.clock.tick(60)

    def display_score(self):
        game_font = pygame.font.SysFont("Arial", 24)
        text = game_font.render(f"Score: {self.score}", True, (255, 0, 0))
        self.window.blit(text, (500, 50))

if __name__ == "__main__":
    
    robot_instance = Robot("robot.png", 0, 480 - 90)  # 90 approximately the height of the robot
    game_instance = Game(640, 480, robot_instance, 8)
    game_instance.run()













    