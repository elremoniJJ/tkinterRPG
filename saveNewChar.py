import random
import stuff
import math
import re

def attackUpdate(char_type, weapon):
    player_type_text = open(f"{char_type}.txt", "r")
    player_attr_lines = player_type_text.readlines()
    player_type_text.close()

    attack = 0

    if player_attr_lines[0][8:] == "Warrior\n":
        attack += math.floor((int(player_attr_lines[1][11:]) / 3) + 3)
        attack += math.floor((int(player_attr_lines[3][6:]) / 4) + 1)

    if player_attr_lines[0][8:] == "Ninja\n":
        attack += math.floor((int(player_attr_lines[1][11:]) / 4) + 1)
        attack += math.floor((int(player_attr_lines[3][6:]) / 3) + 3)

    if player_attr_lines[0][8:] == "Alchemist\n":
        attack += math.floor((int(player_attr_lines[4][14:]) / 2) + 3)
        attack += math.floor((int(player_attr_lines[3][6:]) / 5) + 1)

    if weapon == 'Metal stick':
        attack += 3

    if weapon == 'Dull sword':
        attack += 5

    if weapon == 'Sword':
        attack += 7

    if weapon == 'Sharp sword':
        attack += 9

    if weapon == 'Super sharp sword':
        attack += 11

    if weapon == 'Shuriken':
        attack += 5

    if weapon == 'Bag of gold dust':
        attack += 1

    return attack


def defenseUpdate(char_type):
    player_type_text = open(f"{char_type}.txt", "r")
    player_attr_lines = player_type_text.readlines()
    player_type_text.close()

    defense = 0

    if player_attr_lines[0][8:] == "Warrior\n":
        defense += math.floor((int(player_attr_lines[3][6:]) / 2) + 5)
        defense += math.floor((int(player_attr_lines[1][11:]) / 3) + 3)

    if player_attr_lines[0][8:] == "Ninja\n":
        defense += math.floor((int(player_attr_lines[3][6:]) / 3) + 3)
        defense += math.floor((int(player_attr_lines[1][11:]) / 2) + 5)

    if player_attr_lines[0][8:] == "Alchemist\n":
        defense += math.floor((int(player_attr_lines[4][14:]) / 1.5) + 5)
        defense += math.floor((int(player_attr_lines[3][6:]) / 4) + 3)

    return defense


def saveChar(char_attr_list):
    char_attr_list_total = 0
    for i in char_attr_list:
        if type(i) != int:
            continue
        char_attr_list_total += int(i)

    char_coins = 100 - char_attr_list_total + random.randint(10, 20)
    char_attr_list.append(char_coins)
    char_attr_list.append("")
    char_attr_list.append("")
    char_attr_list.append("")
    char_attr_list.append("0")

    attack = attackUpdate(char_attr_list[0], "")
    defense = defenseUpdate(char_attr_list[0])

    char_attr_list.append(f"{attack}")
    char_attr_list.append(f"{defense}")

    attr_labels = ["Type",
                   "Strength",
                   "Health",
                   "Speed",
                   "Intelligence",
                   "Charisma",
                   "Coins",
                   "Shield",
                   "Health potion",
                   "Weapon",
                   "Monsters killed",
                   "Attack",
                   "Defense"]

    write_char_attr = open(f"{char_attr_list[0]}.txt", "w")
    for i in range(len(char_attr_list)):
        line = f"{attr_labels[i]}:   {char_attr_list[i]}\n"
        write_char_attr.write(line)
    write_char_attr.close()

    return True


def shopPurchase(char_type, item_name, item_price, coins_left):

    def coinage(coins_left):
        coins_left -= int(item_price)
        return f"Coins:   {coins_left}\n"

    player_type_text = open(f"{char_type}.txt", "r")
    player_attr_lines = player_type_text.readlines()
    player_type_text.close()

    if item_name == "Shield":
        if player_attr_lines[7][-3:] == "  \n":
            player_attr_lines[7] = f"{item_name}:   Equipped\n"
            player_attr_lines[6] = coinage(coins_left)
            defense = defenseUpdate(char_type)
            player_attr_lines[12] = f"Defense:   {defense+5}\n"

    if item_name == "Health potion":
        if player_attr_lines[8][-3:] == "  \n":
            player_attr_lines[8] = f"{item_name}:   Equipped\n"
            player_attr_lines[6] = coinage(coins_left)

    char_weapons = ['Sword', 'Shurikens', 'Bag of gold dust']
    for i in char_weapons:
        if item_name == i and player_attr_lines[9][-3:] == "  \n":
            player_attr_lines[9] = f"Weapon:   {item_name}\n"
            player_attr_lines[6] = coinage(coins_left)
            attack = attackUpdate(char_type, i)
            player_attr_lines[11] = f"Attack:   {attack}\n"

    char_weapon_upgrades = ['Sword sharpening',
                            'Shuriken launcher',
                            'Fireplace bellow']
    for i in char_weapon_upgrades:
        if item_name == i and player_attr_lines[9][-3:] != "  \n":
            if re.search('Metal stick', player_attr_lines[9]):
                player_attr_lines[9] = f"Weapon:   Dull sword\n"
                player_attr_lines[6] = coinage(coins_left)
                attack = attackUpdate(char_type, "Dull sword")
                player_attr_lines[11] = f"Attack:   {attack}\n"
                break

            if re.search('Dull sword', player_attr_lines[9]):
                player_attr_lines[9] = f"Weapon:   Sword\n"
                player_attr_lines[6] = coinage(coins_left)
                attack = attackUpdate(char_type, "Sword")
                player_attr_lines[11] = f"Attack:   {attack}\n"
                break

            if re.search('Sword', player_attr_lines[9]):
                player_attr_lines[9] = f"Weapon:   Sharp sword\n"
                player_attr_lines[6] = coinage(coins_left)
                attack = attackUpdate(char_type, "Sharp sword")
                player_attr_lines[11] = f"Attack:   {attack}\n"
                break

            if re.search('Sharp sword', player_attr_lines[9]):
                player_attr_lines[9] = f"Weapon:   Super sharp sword\n"
                player_attr_lines[6] = coinage(coins_left)
                attack = attackUpdate(char_type, "Super sharp sword")
                player_attr_lines[11] = f"Attack:   {attack}\n"
                break

            if re.search('Shurikens', player_attr_lines[9]):
                player_attr_lines[9] = f"Weapon:   Shurikens\n"
                player_attr_lines[6] = coinage(coins_left)
                attack = attackUpdate(char_type, "Shurikans")
                player_attr_lines[11] = f"Attack:   {attack}\n"
                break

            if re.search('Bag of gold dust', player_attr_lines[9]):
                pass

            """
            player_attr_lines[9] = f"Weapon:   {item_name}\n"
            coins_left -= int(item_price)
            player_coins_update = f"Coins:   {coins_left}\n"
            player_attr_lines[6] = player_coins_update
            attack = attackUpdate(char_type, i)
            player_attr_lines[11] = f"Attack:   {attack}\n"
            """

    write_char_attr = open(f"{char_type}.txt", "w")
    for line in player_attr_lines:
        write_char_attr.write(line)
    write_char_attr.close()

    player_equipped_text = ""
    for i in range(6, 13):
        player_equipped_text += player_attr_lines[i]

    return player_equipped_text



