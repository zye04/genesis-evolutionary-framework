from agent import action_enum
from controller import controller_type
import random


class RC:
    def __init__(self):
        self.move = action_enum.Movement.STATIONARY
        self.turn = action_enum.Turn.NONE

        self.move_timer_accumulated = 0
        self.move_timer_threshold = 0.5

        # enum lists
        self.list_movement = list(action_enum.Movement)
        self.list_turn = list(action_enum.Turn)
        self.controller_type = controller_type.Controller.RANDOM

    # Randomly chooses a movement every second
    def rmove(self):
        self.move = random.choice(self.list_movement)

    # Randomly chooses a turn every second
    def rturn(self):
        self.turn = random.choice(self.list_turn)

    # Update controller state
    def update(self, delta_time):
        self.move_timer_accumulated += delta_time
        if self.move_timer_accumulated >= self.move_timer_threshold:
            self.move_timer_accumulated = 0
            self.rmove()
            self.rturn()
