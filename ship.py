import pygame

from constants import PLAYER_MOVE_SPEED, PLAYER_ROTATE_SPEED


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image: pygame.Surface, scale=1):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.angle = 0

        # -y is "forward"
        self.forward = pygame.Vector2(0, -1)
        self.direction = self.forward
        self.velocity = pygame.Vector2(0, 0)
        self.original_image = image
        self.is_idle = True
        self.scale(scale)
        self.update_image()

    def update_image(self):
        self.updated_image = pygame.transform.rotate(self.scaled_image, self.angle)

    def rotate(self, dt):
        self.angle += dt * PLAYER_ROTATE_SPEED
        self.direction = self.forward.rotate(-self.angle)

    def update_velocity(self, dt):
        self.velocity = self.direction * dt * PLAYER_MOVE_SPEED

    def move(self):
        self.position += self.velocity

    def update(self, dt):
        keys = pygame.key.get_pressed()
        forward_key_pressed = False

        if keys[pygame.K_a]:
            self.rotate(dt)

        if keys[pygame.K_d]:
            self.rotate(-dt)

        if keys[pygame.K_w]:
            forward_key_pressed = True
            self.update_velocity(-dt)
            self.move()

        if keys[pygame.K_s]:
            forward_key_pressed = True
            self.update_velocity(dt)
            self.move()

        if not forward_key_pressed:
            self.velocity = pygame.Vector2(0, 0)
            self.is_idle = True
        else:
            self.is_idle = False

        self.update_image()

    def draw(self, screen):
        # need to update this to get rect
        screen.blit(
            self.updated_image, self.updated_image.get_rect(center=self.position)
        )
        # drawing position and direction vectors for show
        pygame.draw.line(screen, "yellow", (0, 0), self.position)
        pygame.draw.line(
            screen,
            "red",
            self.position,
            (
                self.position.x + (self.velocity.x * 20),
                self.position.y + (self.velocity.y * 20),
            ),
        )

    def scale(self, factor):
        self.scaled_image = pygame.transform.scale_by(self.original_image, factor)
        self.updated_image = self.scaled_image
