import random
from constant import *
from button import *

def draw_snake(snake_block, snake_list, window):
    for snake in snake_list:
        pygame.draw.rect(window, "white", [snake[0], snake[1], snake_block, snake_block])

