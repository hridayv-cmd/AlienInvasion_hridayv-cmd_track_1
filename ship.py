
"""
Program Name: Alien Invasion - Player Ship Controller
Author: Hriday Vermani
Purpose: Dictates player ship dimensions, asset transformation rotation rules, 
         and vertical boundary checks along the left screen border.
Starter Code: Cloned from https://github.com/hridayv-cmd/alien_invasion_starter_game.git
Date: July 24 2026
"""


import pygame
from typing import TYPE_CHECKING

# Avoid circular imports while allowing type hinting
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """Manages player ship behavior, movement, rendering, and firing along the vertical axis."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize the ship and set its starting position at bottom-center."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load and scale the player ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_h, self.settings.ship_w) 
            )
        self.image = pygame.transform.rotate(self.image, -90)

        
        # Initialize placement properties
        self.rect = self.image.get_rect()
        self._center_ship()

        # Movement flags to track ongoing key presses
        self.moving_up = False
        self.moving_down  = False
        self.arsenal = arsenal

    def _center_ship(self):
        """Reset the ship back to its starting bottom-center coordinate position."""
        self.rect.midleft = self.boundaries.midleft
        self.y = float(self.rect.y)     # Track precise decimal position for horizontal tracking

    def update(self):
        """Update the ship's position and manage weapon cooling/updates."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Adjust the ship's horizontal position while keeping it in screen boundaries."""
        temp_speed = self.settings.ship_speed
        
        # Move right if flag is active and ship hasn't hit the right boundary
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed

            # Move left if flag is active and ship hasn't hit the left boundary
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        # Sync the structural layout rect position with the floating mathematical variable
        self.rect.y = self.y


    def draw(self) -> None:
        """Draw the ship on screen at its current position."""
        self.screen.blit(self.image, self.rect )


    def fire(self):
        """Request the weapon arsenal to fire a bullet."""
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        """Detect individual contact hits with elements like the alien fleet group."""
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()     # Snap back to center upon taking damage
            return True
        return False
    