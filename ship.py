import pygame
from bullet import Bullet
from sprite_images import bullet_img
import math

from constants import *


def draw_arrow(screen, start, end, color, arrow_size=10, width=2):
    # Draw the main line
    pygame.draw.line(screen, color, start, end, width)

    # Calculate the direction of the arrow
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    angle = math.atan2(dy, dx)

    # Calculate the points for the arrowhead
    arrow_point1 = (
        end[0] - arrow_size * math.cos(angle - math.pi / 6),
        end[1] - arrow_size * math.sin(angle - math.pi / 6),
    )
    arrow_point2 = (
        end[0] - arrow_size * math.cos(angle + math.pi / 6),
        end[1] - arrow_size * math.sin(angle + math.pi / 6),
    )

    pygame.draw.polygon(screen, color, [end, arrow_point1, arrow_point2])


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
        self.scale(scale)
        self.update_image()
        self.shoot_cooldown = 0

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
        self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(dt)

        if keys[pygame.K_d]:
            self.rotate(-dt)

        if keys[pygame.K_w]:
            self.update_velocity(-dt)
            self.move()

        if keys[pygame.K_s]:
            self.update_velocity(dt)
            self.move()

        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown > 0:
                return
            b = Bullet(
                self.position.x,
                self.position.y,
                pygame.transform.rotate(bullet_img, self.angle),
            )
            # why does need dt need to be negative???
            b.velocity = self.forward.rotate(-self.angle) * 300 * -dt
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def draw(self, screen):
        # need to update this to get rect
        self.update_image()
        screen.blit(
            self.updated_image, self.updated_image.get_rect(center=self.position)
        )
        """
        pygame.draw.rect(
            screen, "red", self.updated_image.get_rect(center=self.position), 2
        )
        # drawing position and direction vectors for show
        draw_arrow(screen, (0, 0), self.position, "yellow")
        draw_arrow(
            screen,
            self.position,
            (
                self.position.x + (self.velocity.x * 20),
                self.position.y + (self.velocity.y * 20),
            ),
            "red",
        )
        
        """

    def scale(self, factor):
        self.scaled_image = pygame.transform.scale_by(self.original_image, factor)
        self.updated_image = self.scaled_image
