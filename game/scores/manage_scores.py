import json
import os
from game.__settings__ import SCORE_PATH
'''
'''
def combo_count(played_key, last_key, score, combo):
    if played_key == last_key:
        if combo <= 2:
            score += 2
            combo += 1
        elif combo <= 5:
            score += round(combo*0.8)
            combo +=1
        else:
            score += 3
            combo +=1
        return score, combo
    else :
        score += 1
        combo = 0
        return score, combo

'''
player_id : Checks if the player's ID exists in the scores dictionary. 
If not, initializes the player's record with default values and saves the scores.
}
'''
def create_player(player, scores):
    if player not in scores:
        # Initialize the player's record with default values
        scores[player] = {'highscore': 0, 'slashed_fruits': 0, 'games_played': 0}
        save_scores(scores)
'''
Load_scores : Loads the scores from the JSON file. 
If the file does not exist, it creates an empty JSON file.
'''
def load_scores():
    if not os.path.exists(SCORE_PATH):
        # Create an empty JSON file if it doesn't exist
        with open(SCORE_PATH, "w", encoding="UTF-8") as file:
            json.dump({}, file)
    # Read and load the scores from the file
    with open(SCORE_PATH, "r") as file:
        scores = json.load(file)
    return scores
'''
Save_scores : Saves the scores dictionary to the JSON file.
'''
def save_scores(scores):

    with open(SCORE_PATH, "w") as file:
        json.dump(scores, file, indent=4)
'''
Update_scores : Updates the scores for a player based on the game result.
'''
def update_scores(score, slashed, player):
    # Load the current scores
    scores = load_scores()
    player = str(player).lower()
    # Ensure the player's record exists
    create_player(player, scores)
    if scores[player]['highscore'] < score:
        scores[player]['highscore'] = score
    scores[player]['slashed_fruits'] += slashed
    scores[player]['games_played'] +=1
    # Save the updated scores
    save_scores(scores)
'''
erase_all_record : Deletes the score file, erasing all records.
'''
def erase_all_record():
    os.remove(SCORE_PATH)