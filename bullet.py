"""
Program Name: Alien Invasion - Laser Bullet Sprite
Author: Hriday Vermani
Purpose: Handles individual laser projectile generation, rotation transformations, 
         and horizontal coordinate positioning loops.
Starter Code: Cloned from https://github.com/hridayv-cmd/alien_invasion_starter_game.git
Date: July 2026
"""



import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

# Avoid circular imports while allowing type hinting
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """A class to manage laser bullets fired horizontally from the player's ship."""
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the bullet sprite and set its starting position."""
        super().__init__()
        
        self.screen = game.screen
        self.settings = game.settings

        # Load the bullet graphic and scale it to the size specified in settings
        base_image = pygame.image.load(self.settings.bullet_file)
        rotated_image = pygame.transform.rotate(base_image, -90)
        self.image = pygame.transform.scale(rotated_image,
            (self.settings.bullet_w, self.settings.bullet_h) 
            )
        
        # Position the bullet at the top-middle of the ship
        self.rect = self.image.get_rect()
        self.rect.midright = game.ship.rect.midright
        self.rect.x += 15
        # Store a decimal value for precise vertical movement tracking
        self.x = float(self.rect.x)


    def update(self):
        """Move the bullet vertically up the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet image on the screen at its current position."""
        self.screen.blit(self.image, self.rect)