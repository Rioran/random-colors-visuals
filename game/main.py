import asyncio
import sys

import pygame


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()

    colors = ('yellow', 'blue', 'red')
    color_index = 0

    while True:
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            if event.key == pygame.K_SPACE:
                color_index = (color_index + 1) % len(colors)
                new_color = colors[color_index]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        clock.tick(25)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
