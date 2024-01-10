from enum import Enum

WIDTH = 800
HEIGHT = 600
SCREEN = (WIDTH, HEIGHT)

SNAKE_BLOCK = 20
SNAKE_SPEED = 10

class STATE(Enum):
    INIT = 1
    GET_INPUT = 2
    PLAYING = 3
    END = 4