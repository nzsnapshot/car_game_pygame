import pygame




class Car():
    """A class to manage the car."""

    def __init__(self, ai_game):
        """Initialize the car and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the car image and get its rect.
        self.image = pygame.image.load('imgs/car.png')
        self.rect = self.image.get_rect()

        # Start each new car at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        self.moving_forward = False
        self.moving_backwards = False

    def update(self):
        """Update the car's position based on movement flags."""
        # Update the car's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.car_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.car_speed
        
        # if self.moving_forward and self.rect.top > 0:
        #     self.y -= self.settings.car_speed
        # if self.moving_backwards and self.rect.bottom > 0:
        #     self.y += self.settings.car_speed
        if self.moving_forward:
            self.y -= self.settings.car_speed
        if self.moving_backwards:
            self.y += self.settings.car_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the car at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_car(self):
        """Center the car on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
