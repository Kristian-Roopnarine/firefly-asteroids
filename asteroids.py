import random
import pygame


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, img, scale=1):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.scale_factor = scale
        self.original_image = img
        self.angle = 0
        self.rotation_speed = random.randint(0, 360)

    def update(self, dt):
        self.position += self.velocity * dt
        self.angle += self.rotation_speed * dt

    def draw(self, screen):
        rotated_img = pygame.transform.rotate(self.original_image, self.angle)
        scaled_img = pygame.transform.scale_by(rotated_img, self.scale_factor)
        screen.blit(scaled_img, scaled_img.get_rect(center=self.position))
