import sys

import pygame
from settings import Settings

from starsimg import Star_img

class Stars_sky:
    """Overall class to manage stars on screen"""
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('stars in the sky')

        self.stars = pygame.sprite.Group()
        self._create_stars()


    def run_game(self):
        """Start the main loop for the project"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit()
             elif event.type == pygame.KEYDOWN:
                 self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to key_down events"""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_stars(self):
        """Create a sky full of stars."""
        #Create a star and keep adding stars untill there's no room left.
        #Spacing between stars is two star widths.
        star = Star_img(self)
        star_width, star_height = star.rect.size

        current_x, current_y = 2 * star_width, 2 * star_height
        while current_y < (self.settings.screen_height - (3 * star_height)):
            while current_x < (self.settings.screen_width - (2 * star_width)):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            #Finish a row; reset x value, and increment y value.
            current_x = 2 * star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the grid"""
        new_star = Star_img(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        #Make the most recently drawn screen visible
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    """make a game instance and run the game"""
    star = Stars_sky()
    star.run_game()
    