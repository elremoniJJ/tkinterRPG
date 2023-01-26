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
    return player_attr, player_attr_lines

def coinflip():
    return random.randint(0,1)


def initAttack(player_attr, goblin_attr):
    player_init_attack = (math.floor(0.5 * player_attr[4]) + player_attr[3])
    monst_init_attack = (math.floor(0.5 * goblin_attr.get('goblin_intelligence'))
                         + goblin_attr.get('goblin_speed'))

    if player_init_attack > monst_init_attack:
        return True

    elif player_init_attack < monst_init_attack:
        print(f"{goblin_attr.get('type')} attacks first")
        return False

    else:
        result = coinflip()
        if result == 1:
            return True
        else:
            return False


def doDamage(attack, health):
    print("Player doing damage")
    health -= attack
    if health < 1:
        print("Goblin is dead")
        ######################
        # Where the file should be updated
        ######################
        return "Dead"
    else:
        print(f"Goblin health: {health}")
        return health


def takeDamage(attack, defense, health, player_attr_lines):
    print("Player taking damage")
    damage = attack - defense
    if damage < 1:
        return player_attr_lines
    else:
        health -= damage
        if health < 1:
            return "You died"
        player_attr_lines[2] = f"Health:   {health}\n"
        return player_attr_lines


def battle(char_type, num_monsters_killed):

    player_attr, player_attr_lines = getPlayer(char_type)

    goblin_attr = getMonster()
    initialAttack = initAttack(player_attr, goblin_attr)

    if initialAttack:
        # Player attacks first
        result = doDamage(player_attr[6], goblin_attr.get('goblin_health'))
        if result == "Dead":
            num_monsters_killed += 1
            print(f" - You killed {num_monsters_killed} {goblin_attr.get('type')}")
            return num_monsters_killed

        else:
            player_attr_lines_update = takeDamage(goblin_attr.get('goblin_strength'),
                                                  player_attr[7],
                                                  player_attr[2],
                                                  player_attr_lines)
            if player_attr_lines_update == "You died":
                return player_attr_lines_update

            write_char_attr = open(f"{char_type}.txt", "w")
            for line in player_attr_lines_update:
                write_char_attr.write(line)
            write_char_attr.close()
            return "-1"

    else:
        player_attr_lines_update = takeDamage(goblin_attr.get('goblin_strength'),
                            player_attr[7],
                            player_attr[2],
                            player_attr_lines)
        if player_attr_lines_update == "You died":
            return player_attr_lines_update

        write_char_attr = open(f"{char_type}.txt", "w")
        for line in player_attr_lines_update:
            write_char_attr.write(line)
        write_char_attr.close()

        result = doDamage(player_attr[6], goblin_attr.get('goblin_health'))
        if result == "Dead":
            num_monsters_killed += 1
            print(f" - - You killed {num_monsters_killed} {goblin_attr.get('type')}")
            return num_monsters_killed
        else:
            return int("-1")
