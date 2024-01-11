from enum import Enum

WIDTH = 800
HEIGHT = 600
SCREEN = (WIDTH, HEIGHT)

SNAKE_BLOCK = 20
SNAKE_SPEED = 15

class STATE(Enum):
    MENU = 1
    PLAYING = 2
    END = 3