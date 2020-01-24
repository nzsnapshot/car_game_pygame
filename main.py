import sys
import pygame
from car import Car
from settings import Settings
from dinosaur import Dinosaur

class SnapStrats:
    """Overall class to manage game assests and behaviours"""
    def __init__(self):
        """Initilize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snap Strats")
        self.dinosaur = Dinosaur(self)
        self.car = Car(self)
        self.dinosaurs = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        """Create the cars"""
        # Create an alien and find the number of aliens in a rrow.
        dinosaur = Dinosaur(self)
        dinosaur_height = dinosaur.rect.height
        available_space_y = self.settings.screen_height - (2 * dinosaur_height)
        number_dinosaurs_y = available_space_y // (2 * dinosaur_height)

        # Create the first row of dino saurs
        for dinosaur_number in range(number_dinosaurs_y):
            dinosaur = Dinosaur(self)
            dinosaur.y = dinosaur_height + 2 * dinosaur_height * dinosaur_number
            dinosaur.rect.y = dinosaur.y

            self.dinosaurs.add(dinosaur)



    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.car.update()
            self.dinosaur.update()
            self._update_screen()
            self._update_dinosaurs()
            # Watch for keyboard and mouse events.

    def _update_dinosaurs(self):
        """Update the position of the dinosaurs"""
        self._check_fleet_edges()
        self.dinosaurs.update()

    def _check_fleet_edges(self):
        """Respoind appropriately if any dinosauars have reached the edgee"""
        for dino in self.dinosaurs.sprites():
            if dino.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleets direction"""
        self.settings.fleet_direction *= -1




    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def  _check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = True
        elif event.key == pygame.K_UP:
            self.car.moving_forward = True
        elif event.key == pygame.K_DOWN:
            self.car.moving_backwards = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = False
        elif event.key == pygame.K_UP:
            self.car.moving_forward = False
        elif event.key == pygame.K_DOWN:
            self.car.moving_backwards = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.settings.bg_image,(0,0) )
        self.car.blitme()
        self.dinosaurs.draw(self.screen)
        #
        pygame.display.flip()

if __name__ == '__main__':
    ss = SnapStrats()
    ss.run_game()