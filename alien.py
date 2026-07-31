"""
Program Name: Alien Invasion - Alien Enemy Unit
Author: Hriday Vermani
Purpose: Tracks mathematical vectors, graphics loading, and collision borders 
         for an individual invader unit.
Starter Code: Cloned from https://github.com/hridayv-cmd/alien_invasion_starter_game.git
Date: July 24 2026
"""


import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

# Avoid circular imports while allowing type hinting for the fleet controller
if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, fleet: 'AlienFleet', x: float, y:float ):
        """Initialize the alien unit and set its starting coordinates on the grid."""
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings
        
       # Load and scale the alien image asset based on game configuration settings
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_w, self.settings.alien_h) 
            )
        
        # Position the asset rectangle tracking dimensions using parameters passed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
        # Store precise decimal values for granular movement tracking vectors
        self.y = float(self.rect.y)
        self.x = float(self.rect.x) 


    def update(self):
        """Move the alien horizontally left towards the player's ship."""
        self.x -= self.settings.alien_speed_x
        self.rect.x = self.x

        # Keep the drawing hitbox vertically aligned with its self.y coordinate
        self.rect.y = self.y





    
    def check_edges(self):
        """Return True if the element boundary overlaps or collides with the screen frame boundaries."""
        return (self.rect.bottom >= self.screen.get_rect().bottom) or (self.rect.top <= self.screen.get_rect().top)


    def draw_alien(self):
        """Render the alien graphic onto the active screen plane layout."""
        self.screen.blit(self.image, self.rect)