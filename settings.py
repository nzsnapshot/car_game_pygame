import pygame


class Settings:
    """A Class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.bg_image = pygame.image.load('imgs/bg_image.png')

        # Car's speed
        self.car_speed = 5

        # Dinosaurs speed
        self.dinosaur_speed = 5
        self.fleet_direction = 1




