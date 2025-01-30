import json
import os

def load_scores():
    if not os.path.exists('scores.json'):
        print("Error: The file scores.json was not found. Creating a default file.")
        return {"players": [], "menu_options": {"view_scores": True, "add_player": True, "clear_history": True, "view_history": True}, "game_settings": {}}
    else:
        with open('scores.json', 'r') as f:
            return json.load(f)

def save_scores(data):
    try:
        with open('scores.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully!")
    except Exception as e:
        print(f"Error while saving data: {e}")

def display_scores(data):
    if 'players' not in data:
        print("No players found.")
        return
    players = sorted(data['players'], key=lambda x: x['wins'], reverse=True)
    print("\nPlayer Rankings:")
    for player in players:
        print(f"{player['name']} - Wins: {player['wins']} - Fruits Sliced: {player['fruits_sliced']}")

def add_player(data):
    name = input("Enter the new player's name: ")
    data['players'].append({
        "name": name,
        "win_streak": 0,
        "losses": 0,
        "mistakes": 0,
        "wins": 0,
        "fruits_sliced": 0,
        "level": 0,
        "time_remaining": 0,
        "history": []
    })
    save_scores(data)
    print(f"Player {name} added successfully!")

def view_history(data):
    name = input("Enter the player's name whose history you want to see: ")
    for player in data['players']:
        if player['name'] == name:
            print(f"\nHistory of {name}:")
            for entry in player['history']:
                print(f"Date: {entry['date']} - Score: {entry['score']} - Level: {entry['level']} - Mode: {entry['mode']}")
            return
    print("Player not found.")

def clear_history_and_player(data):
    name = input("Enter the player's name whose history and data you want to delete: ")
    for player in data['players']:
        if player['name'] == name:
            data['players'].remove(player)
            save_scores(data)
            print(f"Player {name} and their history have been deleted.")
            return
    print("Player not found.")

def game_settings(data):
    print("\nModify Game Settings:")
    difficulty = input("Choose difficulty (Easy, Medium, Hard): ")
    time_limit = input("Choose time limit in seconds: ")
    game_speed = input("Choose game speed (Slow, Normal, Fast): ")
    sounds = input("Enable sounds? (yes/no): ").lower() == 'yes'
    visual_effects = input("Enable visual effects? (yes/no): ").lower() == 'yes'
    pause = input("Allow pause in-game? (yes/no): ").lower() == 'yes'
    
    data['game_settings'] = {
        "difficulty": difficulty,
        "time_limit": int(time_limit) if time_limit.isdigit() else 0,
        "game_speed": game_speed,
        "sounds": sounds,
        "visual_effects": visual_effects,
        "pause": pause
    }
    
    save_scores(data)
    print("Game settings have been updated.")

def menu():
    data = load_scores()
    while True:
        print("\n === Menu === :")
        print("\n1. View player scores")
        print("2. Add a player")
        print("3. View a player's history")
        print("4. Delete player history and data")
        print("5. Game settings")
        print("6. Quit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            display_scores(data)
        elif choice == '2':
            add_player(data)
        elif choice == '3':
            view_history(data)
        elif choice == '4':
            clear_history_and_player(data)
        elif choice == '5':
            game_settings(data)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

menu()




