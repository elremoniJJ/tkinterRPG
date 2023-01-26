from random import randint


def goblin():
    goblin = {
        "type": "Goblin",
        "goblin_strength": randint(14, 21),
        "goblin_health": randint(6, 12),
        "goblin_speed": randint(12, 16),
        "goblin_intelligence": randint(14, 15),
        "goblin_charisma": randint(5, 10)
    }
    return goblin


def orc():
    orc = {
        'type': 'Orc',
        'orc_strength': randint(13, 18),
        'orc_health': randint(15, 18),
        'orc_speed': randint(7, 12),
        'orc_intelligence': randint(4, 8),
        'orc_charisma': randint(2, 6)
    }
    return orc


def elvish_bounty_hunter():
    ebh = {
        'Elvish Bounty Hunter': 'Elvish Bounty Hunter',
        'elvish_bounty_hunter_strength': randint(12, 15),
        'elvish_bounty_hunter_health': randint(12, 15),
        'elvish_bounty_hunter_speed': randint(12, 17),
        'elvish_bounty_hunter_intelligence': randint(12, 15),
        'elvish_bounty_hunter_charisma': randint(15, 18)
    }
    return ebh


def magical_gnome():
    maggnome = {
        'type': 'Magical Gnome',
        'magical_gnome_strength': randint(6, 8),
        'magical_gnome_health': randint(10, 12),
        'magical_gnome_speed': randint(8, 17),
        'magical_gnome_intelligence': randint(16, 20),
        'magical_gnome_charisma': randint(5, 20)
    }
    return maggnome

#Yourself


