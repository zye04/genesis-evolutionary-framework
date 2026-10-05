import math
import pygame
from agent.visible_entity import VisibleEntity


class Vision:
    def __init__(self, range, fov):
        self.range = range
        self.fov = fov

    def observe(self, ant, entities):
        entities_visible = []

        for entity in entities:
            vec_x = entity.x - ant.x
            vec_y = entity.y - ant.y
            distance = math.sqrt((vec_x**2) + (vec_y**2))

            angle = math.atan2(vec_y, vec_x)

            angle_degrees = math.degrees(angle)

            diff = (angle_degrees - ant.angle) % 360
            if diff > 180:
                diff = diff - 360
            if distance <= self.range and abs(diff) <= (self.fov / 2):
                entities_visible.append(
                    VisibleEntity(
                        entity.entity_type, entity.x, entity.y, distance, diff
                    )
                )

        return entities_visible

    # Draw the field of view of the Ant
    def draw(self, screen, ant):
        color = (180, 180, 255)
        screen_x = ant.x
        screen_y = screen.get_height() - ant.y

        for edge_angle in (ant.angle + self.fov / 2, ant.angle - self.fov / 2):
            edge_radians = math.radians(edge_angle)
            edge_x = ant.x + math.cos(edge_radians) * self.range
            edge_y = ant.y + math.sin(edge_radians) * self.range
            pygame.draw.line(
                screen,
                color,
                (screen_x, screen_y),
                (edge_x, screen.get_height() - edge_y),
            )

        # pygame.draw.arc measures angles anti-clockwise on screen, which matches our y-up world
        rect = pygame.Rect(0, 0, self.range * 2, self.range * 2)
        rect.center = (screen_x, screen_y)
        start = math.radians(ant.angle - self.fov / 2)
        stop = math.radians(ant.angle + self.fov / 2)
        pygame.draw.arc(screen, color, rect, start, stop, 1)
