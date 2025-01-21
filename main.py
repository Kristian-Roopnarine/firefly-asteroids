import pygame
from constants import *
from ship import Ship
from sprite_sheet import SpriteSheet

# save assets in a folder
# load assets here


# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    firefly_sheet = SpriteSheet("./assets/firefly-32-down.png")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    firefly_image = firefly_sheet.image_at((0, 0, 32, 32))
    Ship.containers = (updatable, drawable)
    firefly = Ship(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, firefly_image, scale=2)
    dt = 0
    clock = pygame.time.Clock()

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
