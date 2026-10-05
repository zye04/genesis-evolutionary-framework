import pygame
import math


class Simulation:
    def __init__(self, width, height, framerate):
        self.running = True
        self.clock = pygame.time.Clock()
        self.framerate = framerate
        self.screen = pygame.display.set_mode((width, height))
        self.ants = []
        self.foods = []

    # Calculate time within the simulation
    def calculate_time(self):
        # delta_time is the time in seconds that passed
        self.delta_time = self.clock.tick(self.framerate) / 1000

    # Update frames within the simulation
    def update(self):
        for ant in self.ants:
            visible = ant.vision.observe(ant, self.foods)
            ant.update(self.delta_time, visible)
            ant.clamp(self.screen)

            for food in self.foods.copy():
                d = self.distance(ant.x, food.x, ant.y, food.y)

                if d <= 28:
                    ant.eat(food)
                    self.foods.remove(food)

    # Draw things on the simulation
    def draw(self):
        self.screen.fill((255, 255, 255))

        for ant in self.ants:
            ant.vision.draw(self.screen, ant)
            ant.draw(self.screen)

        for food in self.foods:
            food.draw(self.screen)

        pygame.display.flip()

    def distance(self, x1, x2, y1, y2):
        d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        return d

    # Event handler
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    # Runner Function for the simulation Object
    def run(self):
        while self.running is True:
            self.calculate_time()
            self.update()
            self.draw()
            self.event_handler()
