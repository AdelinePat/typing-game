import json, os
from __settings__ import SCORE_PATH

class Scores:
    def __init__(self):
        if not os.path.exists(SCORE_PATH):
            # Create an empty JSON file if it doesn't exist
            with open(SCORE_PATH, "w", encoding="UTF-8") as file:
                json.dump({}, file)
        with open(SCORE_PATH, "r") as file:
            self.scores = json.load(file)

    def create_player(self, player):
        '''
        check if the player exists in scores dictionary and initializes 
        their record with default values if needed
        '''
        if player not in self.scores:
            # Initialize the player's record with default values
            self.scores[player] = {'highscore': 0, 'slashed_fruits': 0, 'games_played': 0}
            self.save_scores()

    def save_scores(self):
        '''
        saves the scores dictionary to the dedicated JSON file
        '''
        with open(SCORE_PATH, "w") as file:
            json.dump(self.scores, file, indent=4)

    def update_scores(self, current_player):
        '''
        updates the scores for a player based on the game result
        '''
        # Load the current scores
        player = str(current_player.player).lower()
        # Ensure the player's record exists
        self.create_player(player)
        if self.scores[player]['highscore'] < current_player.score:
            self.scores[player]['highscore'] = current_player.score
        self.scores[player]['slashed_fruits'] += current_player.slashed
        self.scores[player]['games_played'] +=1
        # Save the updated scores
        self.save_scores()

    def erase_all_record():
        '''
        delete the score file, erasing all records
        '''
        os.remove(SCORE_PATH)