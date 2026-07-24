
"""
Program Name: Alien Invasion - Heads Up Display (HUD)
Author: Hriday Vermani
Purpose: Formats and renders game statistic surfaces including high scores, 
         current levels, and remaining player live icons.
Starter Code: Cloned from https://github.com/hridayv-cmd/alien_invasion_starter_game.git
Date: July 24 2026
"""

import pygame.font
#from alien_invasion import AlienInvasion
#from typing import TYPE_CHECKING


# Avoid circular imports while allowing type hinting
#if TYPE_CHECKING:



class HUD:
    """Manages visual scoreboards, level progression cards, and remaining player life trackers."""
    def __init__(self, game):
        """Initialize HUD attributes, set font styles, and build the initial display layout."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats

        # Configure text rendering system using font metrics from settings
        self.font = pygame.font.Font(self.settings.font_file, 
                self.settings.HUD_font_size)

        # Pixel spacing margin used to keep text from touching window edges
        self.padding = 20

        # Pre-render text graphics and life containers
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self):
        """Prepare, scale, and rotate the texture tracking remaining player lives."""

        # Adjust proportions to match current game requirements
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.ship_w, self.settings.ship_h
            ))

        
       # Rotate the life indicator icon -90 degrees to point right, matching the player's active ship
        self.life_image = pygame.transform.rotate(self.life_image, -90)
        self.life_rect = self.life_image.get_rect()

    


    def update_scores(self):
        """Trigger update updates across all system score categories."""
        self._update_score()
        self._update_hi_score()
        self._update_max_score()

    def _update_score(self):
        """Convert the session running score value into a rendered text image panel."""
        score_str = f'Score {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True,
            self.settings.text_color, None)

        # Align the score panel near the top-right corner, positioned below the Max Score panel
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.score_rect.bottom + self.padding


    def _update_max_score(self):
        """Convert the user's all-time historical best score record into a rendered text image panel."""
        max_score_str = f'Max-Score {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True,
            self.settings.text_color, None)

        # Place the maximum session benchmark record strictly in the extreme upper right corner
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        """Convert the running high score cap to match high score limits into a rendered text image panel."""
        hi_score_str = f'Hi-Score {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True,
            self.settings.text_color, None)

        # Anchor the primary high score leaderboard at the absolute top center of the active display window
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx,self.padding)


    def update_level(self):
        """Convert the current level wave index count into a rendered text image panel."""
        level_str = f'Level {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True,
            self.settings.text_color, None)

        # Pin the difficulty tracking layer directly below the player's remaining life indicator row
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding


    def _draw_lives(self):
        """Render a horizontal row of miniature ship images indicating remaining player attempts."""
        current_x = self.padding
        current_y = self.padding


        # Loop through the inventory value to stitch mini-ship assets side-by-side
        for _ in range(self.game_stats.ship_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding



    def draw(self):
        """Blit all pre-rendered HUD elements onto the active screen framework."""
        self.screen.blit(self.hi_score_image,self.hi_score_rect)
        self.screen.blit(self.max_score_image,self.max_score_rect)
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self._draw_lives()
        