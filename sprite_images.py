import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from sprite_sheet import SpriteSheet

if pygame.display.get_init() == False:
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
firefly_sheet = SpriteSheet("./assets/firefly-32-down.png")
bullet_sheet = SpriteSheet("./assets/bullet.png")
big_asteroid_sheet = SpriteSheet("./assets/big-asteroid.png")
medium_asteroid_sheet = SpriteSheet("./assets/med-asteroid.png")
small_asteroid_sheet = SpriteSheet("./assets/small-asteroid.png")

bullet_img = bullet_sheet.image_at((0, 0, 8, 8), (0, 0, 0))
firefly_image = firefly_sheet.image_at((0, 0, 32, 32), (0, 0, 0))
big_asteroid_img = big_asteroid_sheet.image_at((0, 0, 32, 32), (0, 0, 0))
medium_asteroid_img = medium_asteroid_sheet.image_at((0, 0, 16, 16), (0, 0, 0))
small_asteroid_img = small_asteroid_sheet.image_at((0, 0, 8, 8), (0, 0, 0))
