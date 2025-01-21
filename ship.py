import pygame

from constants import PLAYER_ROTATE_SPEED


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image: pygame.Surface, scale=1):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = 0
        self.angle = 0

        # -y is "forward"
        self.direction = pygame.Vector2(0, -1)
        self.original_image = image
        self.scale(scale)
        self.update_image()

    def update_image(self):
        self.updated_image = pygame.transform.rotate(self.scaled_image, self.angle)

    def rotate(self, dt):
        self.angle += dt * PLAYER_ROTATE_SPEED
        # creates a new surface with a scaled image each time this is called
        # can we just rotate the surface or rect?

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)

        if keys[pygame.K_d]:
            self.rotate(-dt)

        if keys[pygame.K_w]:
            pass

        if keys[pygame.K_s]:
            pass

        self.update_image()

    def draw(self, screen):
        # need to update this to get rect
        screen.blit(
            self.updated_image, self.updated_image.get_rect(center=self.position)
        )

    def scale(self, factor):
        self.scaled_image = pygame.transform.scale_by(self.original_image, factor)
        self.updated_image = self.scaled_image
