import pygame
from pygame.sprite import Sprite


class Dinosaur(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('imgs/dinosaurs.png')
        self.rect = self.image.get_rect()
        self.rect.centery = 500
        self.rect.centerx = 300

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if car is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the car to the right"""
        self.x += (self.settings.dinosaur_speed * self.settings.fleet_direction)
        self.rect.x = self.x
