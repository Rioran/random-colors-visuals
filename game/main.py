import asyncio
import sys

import pygame

from utilities.constants import (
    MAX_FPS,
    HEIGHT,
    WIDTH,
    GAME_CAPTION,
    SQUARE_WIDTH,
    SQUARE_HEIGHT,
    CLICK_EVENT_TYPES,
    MAX_COLOR_SHIFT,
    SQUARES_TO_UPDATE_PER_TICK,
)
from utilities.randomize import (
    get_random_color,
    get_random_grid_position,
)
from utilities.functions import (
    check_types_or_keys,
    update_shifts_inplace,
)


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
            image.fill(get_random_color(shifts))
            update = screen.blit(image, get_random_grid_position())
            pygame.display.update(update)
        pointer = update_shifts_inplace(shifts, pointer)

        for event in pygame.event.get():
            if check_types_or_keys(event, CLICK_EVENT_TYPES, pygame.K_SPACE):
                screen.fill('black')
                pygame.display.update()
            elif check_types_or_keys(event, pygame.QUIT, pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        clock.tick(MAX_FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
