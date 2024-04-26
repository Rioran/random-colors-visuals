from typing import Final

import pygame


MAX_FPS: Final = 25
HEIGHT: Final = 400
WIDTH: Final = 600
GAME_CAPTION: Final = \
    'Nerve smoothing visuals' \
    ' // SPACE or click to reset' \
    ' // ESC to quit'

SQUARE_WIDTH: Final = 20
SQUARE_HEIGHT: Final = 20
CLICK_EVENT_TYPES: Final = (
    pygame.MOUSEBUTTONUP,
    pygame.FINGERUP,
)

MAX_COLOR_SHIFT: Final = 100
MINIMUM_COLOR_VALUE: Final = 100
BASE_COLOR: Final = [MINIMUM_COLOR_VALUE] * 3
COLOR_BASE_VARIABILITY: Final = 50
SQUARES_TO_UPDATE_PER_TICK: Final = 12
