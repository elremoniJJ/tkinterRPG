import re

for_everyone = {"Health potion--10": "Health potion",
                "Shield--30": "Shield"}

warrior_stuff = {"Sword--15": "Sword",
                 "Sword sharpening--5": "Sword sharpening"}

ninja_stuff = {"Shurikens--7": "Shurikens",
               "Shuriken launcher--50": "Shuriken launcher"}

alchemist_stuff = {"Bag of gold dust--10": "Bag of gold dust",
                   "Fireplace bellow--60": "Fireplace bellow"}


# Splitting the value of dictionaries in stuff file

def re_stuff_handler(j):
    item_split = re.split("--", j)
    item_split_name = item_split[0]
    item_split_price = item_split[1]
    return item_split_name, item_split_price
