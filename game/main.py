import asyncio
from functools import cache
from random import randint
import sys
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


@cache
def _tuplize_if_not_container(value):
    if '__iter__' not in dir(value):
        return (value, )
    return value


def _check_types_or_keys(event, types, keys):
    target_types = _tuplize_if_not_container(types)
    if event.type in target_types:
        return True
    if event.type == pygame.KEYUP:
        target_keys = _tuplize_if_not_container(keys)
        return event.key in target_keys
    return False


def _get_random_color(shifts):
    colors = BASE_COLOR.copy()
    for i, shift in enumerate(shifts):
        colors[i] += randint(0, COLOR_BASE_VARIABILITY) + shift
    return colors


def _get_random_grid_position():
    width_positions = WIDTH // SQUARE_WIDTH - 1
    height_positions = HEIGHT // SQUARE_HEIGHT - 1
    position = [
        randint(0, width_positions) * SQUARE_WIDTH,
        randint(0, height_positions) * SQUARE_HEIGHT,
    ]
    return position


def _update_shifts_inplace(data, pointer):
    new_pointer = (pointer + 1) % len(data)
    if not data[pointer] == MAX_COLOR_SHIFT:
        data[pointer] -= 1
    else:
        if not data[new_pointer] == MAX_COLOR_SHIFT:
            data[new_pointer] += 1
        else:
            data[pointer] -= 1
    pointer_upgrade = pointer
    if not data[pointer]:
        pointer_upgrade = new_pointer
    return pointer_upgrade


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(GAME_CAPTION)
    clock = pygame.time.Clock()

    image = pygame.Surface((SQUARE_WIDTH, SQUARE_HEIGHT))
    shifts = [MAX_COLOR_SHIFT, 0, 0]
    pointer = 0

    while True:
        for _ in range(SQUARES_TO_UPDATE_PER_TICK):
            image.fill(_get_random_color(shifts))
            update = screen.blit(image, _get_random_grid_position())
            pygame.display.update(update)
        pointer = _update_shifts_inplace(shifts, pointer)

        for event in pygame.event.get():
            if _check_types_or_keys(event, CLICK_EVENT_TYPES, pygame.K_SPACE):
                screen.fill('black')
                pygame.display.update()
            elif _check_types_or_keys(event, pygame.QUIT, pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        clock.tick(MAX_FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
