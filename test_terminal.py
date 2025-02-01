import os, json
# from __settings__ import SCORE_PATH
SCORE_PATH = "./game/scores/scores.json"

def scores():
    # if not os.path.exists(SCORE_PATH):
    # Create an empty JSON file if it doesn't exist
        # with open(SCORE_PATH, "w", encoding="UTF-8") as file:
        #     json.dump({}, file)
    with open(SCORE_PATH, "r") as file:
        scores = json.load(file)
        return scores
score = scores()

def get_scores_menu_page(score):
    if not score:
        print("y'a pas de scores enregistré")
    else:
        all_player = list(score.keys())
        if len(all_player)%8 != 0:
            number_pages = len(all_player)//8 + 1
        else:
            number_pages = len(all_player)//8
    return all_player, number_pages

        # for index in range(len(all_player)):

def display_scores(score):
    all_player, number_pages = get_scores_menu_page(score)

    index_start_list = []
    index_range_list = []
    # range_list = []
    index_start = 0
    index_range = 8
    for page in range(number_pages):
        # page_range = (index_start, index_range)
        index_start_list.append(index_start)
        index_range_list.append(index_range)
        if index_start +8 < len(all_player):
            index_start += 8
            index_range += 8
        if index_range > len(all_player):
            index_range = len(all_player)
        
    for i in range(index_start_list[0], index_range_list[0]):
        print(all_player[i])
        # print(i)

    # i = 0
    # while i <= len(all_player):
    #     if i in range(index_start_list[i], [index_range_list][i]):
    #         print(f"PAGE {i + 1}")
    #         print(all_player[i])
    #     i +=1


    # while i < len(all_player):
    #     index = 0
    #     if i // 8 == index:
    #         range_test = range_list[index]
    #         print(f"range=  {range_test} ")
    #         index +=1
    #         i+=1
    
        # print(f" index=  {index}")

    # print("hello, word")

    # x = 9+3


# score = scores()
display_scores(score)