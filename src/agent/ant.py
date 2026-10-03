import pygame
import math
from agent.action_enum import Movement, Turn


class Ant:
    # Class constructor
    def __init__(self, x, y, stamina_cap, speed, hunger_cap, images, controller):
        self.x = x
        self.y = y
        self.angle = 0

        self.stamina_cap = stamina_cap
        self.stamina = self.stamina_cap
        self.speed = speed
        self.turn_speed = 90
        self.hunger_cap = hunger_cap
        self.hunger = self.hunger_cap

        self.images = images
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_interval = 0.125

        # Eum constructor state
        self.movement = Movement.FORWARD
        self.turn_direction = Turn.NONE

        # Controller that the Ant object is using
        self.controller = controller

    # Draw Ant
    def draw(self, screen):
        screen_y = screen.get_height() - self.y
        screen_x = self.x

        image = self.images[self.current_frame]
        rotated_image = pygame.transform.rotate(image, self.angle + 90)
        rect = rotated_image.get_rect(center=(screen_x, screen_y))

        screen.blit(rotated_image, rect)

    # Move Ant
    def move(self, dx, dy, speed, delta_time):
        self.x += dx * speed * delta_time
        self.y += dy * speed * delta_time

    # Turn Ant
    def turn(self, direction, delta_time):
        self.angle += direction * self.turn_speed * delta_time
        self.angle = self.angle % 360

    # Eat Ant
    def eat(self, food):
        self.stamina += food.stamina_restoration
        if self.stamina >= self.stamina_cap:
            self.stamina = self.stamina_cap
        self.hunger += food.hunger_restoration
        if self.hunger >= self.hunger_cap:
            self.hunger = self.hunger_cap

    # Clamp Position
    def clamp(self, screen):
        half_width = self.images[self.current_frame].get_width() / 2
        half_height = self.images[self.current_frame].get_height() / 2

        min_x = half_width
        max_x = screen.get_width() - half_width

        min_y = half_height
        max_y = screen.get_height() - half_height

        if self.x <= min_x:
            self.x = min_x
        if self.x >= max_x:
            self.x = max_x

        if self.y <= min_y:
            self.y = min_y
        if self.y >= max_y:
            self.y = max_y

    # Update the Ant
    def update(self, delta_time):
        # Update the delta time of the controller
        # The controller is in charge of the Ants behaviour so the movement and turn are defined through it
        self.controller.update(delta_time)
        self.movement = self.controller.move
        self.turn_direction = self.controller.turn

        # Animate if the Ant is either moving or turning
        if self.movement != Movement.STATIONARY or self.turn_direction != Turn.NONE:
            self.animation_timer += delta_time

            if self.animation_timer >= self.animation_interval:
                self.animation_timer = 0
                self.current_frame += 1
                if self.current_frame >= len(self.images):
                    self.current_frame = 0
        else:
            self.current_frame = 0
            self.animation_timer = 0

        # Turn logic, it the Turn enum value to define if it is turning or not
        self.turn(self.turn_direction.value, delta_time)

        # Hunger and stamina depletion update logic
        self.hunger -= 1 * delta_time
        self.stamina -= 1 * delta_time

        # Convert degree of the angle variable into radians
        angle_radians = math.radians(self.angle)
        dx = math.cos(angle_radians)
        dy = math.sin(angle_radians)
        self.move(dx, dy, self.speed * self.movement.value, delta_time)
