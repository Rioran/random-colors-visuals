import asyncio
from random import randint
import sys

import pygame


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()

    logo: pygame.Surface = pygame.image.load("py-logo.png").convert()

    while True:
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            if event.key == pygame.K_SPACE:
                update = screen.blit(logo, (randint(0, 1000), randint(0, 700)))
                pygame.display.update(update)

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        clock.tick(25)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
