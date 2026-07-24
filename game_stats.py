"""
Program Name: Alien Invasion -  Game Stats Tracker
Author: Hriday Vermani
Purpose: Logs dynamic numerical records during active sessions and handles 
         persistent file read/write loops for high score tracking.
Starter Code: Cloned from https://github.com/hridayv-cmd/alien_invasion_starter_game.git
Date: July 24 2026
"""


from pathlib import Path
import json


from typing import TYPE_CHECKING

# Avoid circular imports while allowing type hinting
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats():
    """Track global runtime statistics and active life balances for the game."""
    
    def __init__(self, game: 'AlienInvasion'):
        """Initialize running state metrics and resource tracking allocations."""
        
        # Total remaining player life counts allowed before game over state
        self.game = game
        self.settings = game.settings

        # Tracks the maximum score reached during the *current gameplay session
        self.max_score = 0

        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Read the all-time records from an external JSON file or establish a clean fallback."""
        self.path = self.settings.scores_file

        # If the high score file exists and holds data, load the existing record
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            if not contents:
                print('File empty')
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)

        # Fallback profile setup if record storage missing
        else:
            self.hi_score = 0
            self.save_scores()
            # Save the file
    
    def save_scores(self):
        """Persist the current high score record out into localized JSON storage."""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:

            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')


    def reset_stats(self):
        """Reset operational numerical values to base defaults upon a session restart."""
        self.ship_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Process score revisions dynamically when sprite projectiles register fleet hits."""
        #Update score
        self._update_score(collisions)
        #Update max_score
        self._update_max_score()
         # update hi_score
        self._update_hi_score()

    def _update_max_score(self):
        """Evaluate and raise the maximum score limits reached within the active runtime window."""
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')
    
    def _update_hi_score(self):
        """Evaluate and override the historical records repository tracker."""
        if self.score > self.hi_score:
            self.hi_score = self.score
        #print(f'Hi: {self.hi_score}')
   
    def _update_score(self, collisions):
        """Iterate over register collisions dictionary matrix to calculate incoming point rewards."""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f'Basic: {self.score}')

    def update_level(self):
        """Advance the difficulty level tier indexing tracker by one integer stage."""
        self.level += 1
        #print(self.level)


    

        

    