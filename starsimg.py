import pygame
from pygame.sprite import Sprite

class Star_img(Sprite):
    """A class to mange the ship"""

    def __init__(self, star_sky):
        """initialize the star and its position"""
        super().__init__()
        self.screen = star_sky.screen

        #Load the star to the screen and get its rect.
        self.image = pygame.image.load("images/star2_20x20.png")
        self.rect = self.image.get_rect()

        #Start each star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height