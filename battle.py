import math
import random
import monster_builds


def getMonster():
    goblin_attr = monster_builds.goblin()
    return goblin_attr

def getPlayer(char_type):
    player_type_text = open(f"{char_type}.txt", "r")
    player_attr_lines = player_type_text.readlines()
    player_type_text.close()

    player_attr = [char_type,
                   int(player_attr_lines[1][-4:-1]),  # Strength
                   int(player_attr_lines[2][-4:-1]),  # Health
                   int(player_attr_lines[3][-4:-1]),  # Speed
                   int(player_attr_lines[4][-4:-1]),  # Intelligence
                   int(player_attr_lines[5][-4:-1]),  # Charisma
                   int(player_attr_lines[11][-4:-1]), # Attack
                   int(player_attr_lines[12][-4:-1])]  # Defense
    return player_attr

def coinflip():
    return random.randint(0,1)


def initAttack(player_attr, goblin_attr):
    player_init_attack = (math.floor(0.5 * player_attr[4]) + player_attr[3])
    monst_init_attack = (math.floor(0.5 * goblin_attr.get('goblin_intelligence'))
                         + goblin_attr.get('goblin_speed'))
    print("\nPlayer init: ", player_init_attack)
    print("\nMonster init: ", monst_init_attack)
    if player_init_attack > monst_init_attack:
        print(f"{player_attr[0]} attack first")
        return True
    elif player_init_attack < monst_init_attack:
        print(f"{goblin_attr.get('type')} attacks first")
        return False
    else:
        result = coinflip()
        if result == 1:
            print(f"{player_attr[0]} attacks first: Lucky")
            return True
        else:
            print(f"{goblin_attr.get('type')} attacks first: Lucky")
            return False


def doDamage(attack, health):
    health -= attack
    if health < 1:
        print("Monster is Dead")
    else:
        print(f"Monster health: {health}")


def takeDamage(attack, defense, health):
    print(f"Take damage\nattack:{attack}\ndefense:{defense}\nHEALTH:{health}")
    damage = attack - defense
    if damage < 1:
        print("Defense too high to take damage")
    else:
        health -= damage
        if health < 1:
            print("You are Dead")
        else:
            print(f"Your health: {health}")


def battle(char_type, num_monsters):

    goblin_attr = getMonster()
    player_attr = getPlayer(char_type)

    initialAttack = initAttack(player_attr, goblin_attr)
    if initialAttack:
        # Player attacks first
        result = doDamage(player_attr[6], goblin_attr.get('goblin_health'))
    else:
        result = takeDamage(goblin_attr.get('goblin_strength'), player_attr[7], player_attr[2])
