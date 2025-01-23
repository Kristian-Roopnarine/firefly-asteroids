import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, img, scale=1):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.original_image = img
        self.velocity = pygame.Vector2(0, 0)
        self.scaled_image = pygame.transform.scale_by(self.original_image, scale)

    def update(self, dt):
        self.position += self.velocity

    def draw(self, screen):
        screen.blit(self.scaled_image, self.scaled_image.get_rect(center=self.position))

    def has_collided(self, obj: pygame.Rect):
        return self.scaled_image.get_rect(center=self.position).colliderect(obj)
