import pygame
from environment.entity_type import Entity_type


class Food:
    def __init__(self, x, y, hunger_restoration, stamina_restoration):
        self.x = x
        self.y = y
        self.hunger_restoration = hunger_restoration
        self.stamina_restoration = stamina_restoration

        self.entity_type = Entity_type.FOOD

    # Draw food in the simulation
    def draw(self, screen):
        screen_x = self.x
        screen_y = screen.get_height() - self.y
        pygame.draw.circle(screen, (255, 0, 0), (screen_x, screen_y), 3)
