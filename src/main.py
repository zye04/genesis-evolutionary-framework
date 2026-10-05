import pygame
from random import randint
from agent.ant import Ant
from agent.vision import Vision
from simulation.simulation import Simulation
from controller.random_controller import RC
from environment.food import Food

pygame.init()

# Simulation Object
sim = Simulation(800, 600, 180)

# Use the png for the ant
ants_png = pygame.image.load("../Ants.png").convert_alpha()

ant_images = []

for frame in range(3):
    ant_image = ants_png.subsurface((810 + frame * 90, 0, 90, 96))
    ant_image = pygame.transform.scale(ant_image, (35, 50))
    ant_images.append(ant_image)

# Creates 1 Ant
for _ in range(1):
    brain_tmp = RC()
    vision_tmp = Vision(150, 140)
    ant_tmp = Ant(
        randint(18, 783), randint(25, 575), 0, 35, 0, ant_images, brain_tmp, vision_tmp
    )
    sim.ants.append(ant_tmp)

# Creates 20 foods
for _ in range(200):
    food_tmp = Food(randint(3, 797), randint(3, 597), 10, 10)
    sim.foods.append(food_tmp)

# Run the simulation
sim.run()

pygame.quit()
