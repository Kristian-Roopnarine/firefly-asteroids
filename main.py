import pygame
from asteroid_field import AsteroidField
from asteroids import Asteroid
from bullet import Bullet
from ship import Ship
from sprite_images import firefly_image
from constants import *


# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Bullet.containers = (bullets, updatable, drawable)
    Ship.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    firefly = Ship(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, firefly_image, scale=3)
    asteroid_field = AsteroidField()

    dt = 0
    clock = pygame.time.Clock()

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)

        for b in bullets:
            for a in asteroids:
                if b.has_collided(a.scaled_rect):
                    print("bullet collided")
                    a.kill()
                    b.kill()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
