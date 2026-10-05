from enum import Enum


class Movement(Enum):
    BACKWARDS = -1
    STATIONARY = 0
    FORWARD = 1


class Turn(Enum):
    ANTI_CLOCKWISE = 1
    NONE = 0
    CLOCKWISE = -1
