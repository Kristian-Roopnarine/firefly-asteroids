import pygame
from constants import *
from sprite_sheet import SpriteSheet

# save assets in a folder
# load assets here


# https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    firefly_sheet = SpriteSheet("./assets/firefly32.png")
    image = firefly_sheet.image_at((0, 0, 32, 32))
    firefly_position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    firefly_angle = 0
    big_image = pygame.transform.scale_by(image, 3)
    rotated_image = pygame.transform.rotate(big_image, firefly_angle)
    rotated_rect = rotated_image.get_rect(center=firefly_position)
    dt = 0
    clock = pygame.time.Clock()

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            firefly_angle += 300 * dt
            rotated_image = pygame.transform.rotate(big_image, firefly_angle)
            rotated_rect = rotated_image.get_rect(center=firefly_position)
        if keys[pygame.K_d]:
            firefly_angle += -1 * 300 * dt
            rotated_image = pygame.transform.rotate(big_image, firefly_angle)
            rotated_rect = rotated_image.get_rect(center=firefly_position)
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, -1).rotate(-firefly_angle)
            firefly_position += forward * dt * 200
            rotated_rect = rotated_image.get_rect(center=firefly_position)
        if keys[pygame.K_s]:
            forward = pygame.Vector2(0, -1).rotate(-firefly_angle)
            firefly_position += forward * -dt * 200
            rotated_rect = rotated_image.get_rect(center=firefly_position)

        screen.blit(rotated_image, rotated_rect)
        pygame.draw.line(screen, "white", (0, 0), firefly_position)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
