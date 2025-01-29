from __settings__ import FRUIT_DICT
import secrets

fruits_list= list(FRUIT_DICT.keys())

index = secrets.randbelow(len(fruits_list))
# print(fruits_list[index])

# print(FRUIT_DICT["apple"]["color"])
# print(index)

test = fruits_list[index]

print(test)
