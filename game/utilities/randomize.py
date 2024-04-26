from random import randint

from .constants import (
    BASE_COLOR,
    COLOR_BASE_VARIABILITY,
    HEIGHT,
    WIDTH,
    SQUARE_WIDTH,
    SQUARE_HEIGHT,
)


def get_random_color(shifts):
    colors = BASE_COLOR.copy()
    for i, shift in enumerate(shifts):
        colors[i] += randint(0, COLOR_BASE_VARIABILITY) + shift
    return colors


def get_random_grid_position():
    width_positions = WIDTH // SQUARE_WIDTH - 1
    height_positions = HEIGHT // SQUARE_HEIGHT - 1
    position = [
        randint(0, width_positions) * SQUARE_WIDTH,
        randint(0, height_positions) * SQUARE_HEIGHT,
    ]
    return position
