"""
Program Name: Alien Invasion - Button Component
Author: Hriday Vermani
Purpose: Generates interactive UI text overlay panels allowing for user input
Starter Code: Cloned from https://github.com/hridayv-cmd/alien_invasion_starter_game.git
Date: July 24 2026
"""


import pygame.font


from typing import TYPE_CHECKING

# Avoid circular imports while allowing type hinting
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
 

class Button:
    """Manages interactive text buttons for menus, interface selection boxes, and gameplay triggers."""
    def __init__(self, game: 'AlienInvasion', msg):
        """Initialize the button's visual dimensions, position coordinates, and pre-render text."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        # Configure button font style using project configuration assets
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)

        # Define the structural sizing dimensions for the base button rectangle
        self.rect = pygame.Rect(0,0,self.settings.button_w, self.settings.button_h)

        # Lock the button position directly into the absolute center of the screen layout
        self.rect.center = self.boundaries.center

        # Render the text string argument into a graphic surface texture
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Convert a standard string into a clean, rendered image panel and center it within the button frame."""

        # Render the message string as a clean surface texture image
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)

        # Properply fit the text graphic rect precisely inside the center points of the button background border
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw(self):
        """Draw the solid background button base and overlay the pre-rendered message graphic on top."""

        # Fill the button background area using specified theme settings palette configurations
        self.screen.fill(self.settings.button_color, self.rect)

        # Blit the overlay text asset directly over the center point coordinates
        self.screen.blit(self.msg_image, self.msg_image_rect)


    def check_clicked(self, mouse_pos):
        """Evaluate if specific cursor mouse position coordinates intersect the button's boundary footprint."""
        # Return True if the cursor bounding box point is resting within our layout box coordinates
        return self.rect.collidepoint(mouse_pos)


