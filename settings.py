"""
Program Name: Alien Invasion Settings Configuration
Author: Hriday Vermani
Purpose: Manages/stores all important game settings for ships,bullets,hud, and aliens
Starter Code: Cloned from https://github.com/hridayv-cmd/alien_invasion_starter_game.git
Date: July 24 2026
"""


from pathlib import Path
class Settings:
    """A class to store all static configuration settings for the game."""

    def __init__(self) -> None:
        # Screen and display settings
        self.name: str = 'Alien Invasion - Track 1'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.20
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # Player ship settings
        self.ship_file = Path.cwd() /'Assets' / 'images' / 'ship2.png'
        self.ship_w = 60
        self.ship_h = 40



        # Weapon and bullet settings
        self.bullet_file = Path.cwd() /'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() /'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() /'Assets' / 'sound' / 'ImpactSound.mp3'
  # Max active bullets allowed on screen at once

        # Alien enemy settings
        self.alien_file = Path.cwd() / 'Assets' / 'Images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1   # 1 represents moving DOWN; -1 represents moving UP
        # How far down the screen the alien drops when hitting a wall



        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)


        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self):
        self.ship_speed = 7
        self.starting_ship_count = 3

        self.bullet_w = 80
        self.bullet_h = 25
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.alien_speed_x = 1.0     # Speed moving LEFT toward the player ship
        self.alien_speed_y = 1.0      # Speed shifting UP/DOWN along the right edge
        self.fleet_drop_speed = 25    # Pushes the fleet closer to the ship (LEFT) on edge hit
        self.alien_points = 50


    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.alien_speed_x *= self.difficulty_scale
        self.alien_speed_y *= self.difficulty_scale
    
   
