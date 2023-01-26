import time
from tkinter import *
import ttkbootstrap as ttk

import random
import re

import Quotes
import character_builds
import monster_builds
import stuff
import saveNewChar
import battle

parent = ttk.Window(themename="darkly")
parent.title("RPG with OpenAI")
parent.geometry("600x500")

# Create frame to show images, (in the meantime display number of monsters killed)
frame1 = ttk.Frame(parent,
                   bootstyle="WARNING",
                   borderwidth=2)
frame1.grid(row=0, column=0, columnspan=3,
            padx=5, pady=5,
            ipadx=3, ipady=4)

# Create frame for info on player static variables
frame2 = ttk.Frame(parent,
                   bootstyle="DANGER",
                   borderwidth=2)
frame2.grid(row=1, column=0,
            padx=5, pady=5,
            ipadx=3, ipady=4)

# Create frame for buttons to shop and go on journey
frame3 = ttk.Frame(parent,
                   bootstyle="INFO",
                   borderwidth=2)
frame3.grid(row=1, column=1,
            padx=5, pady=5,
            ipadx=3, ipady=4)

# Create frame 4 for info on player variables
frame4 = ttk.Frame(parent,
                   bootstyle="PRIMARY",
                   borderwidth=2)
frame4.grid(row=1, column=2,
            padx=5, pady=5,
            ipadx=3, ipady=4)

# Create frame5 for info on shop, journey1 and journey2
frame5 = ttk.Frame(parent,
                   bootstyle="DARK",
                   borderwidth=2)
frame5.grid(row=2, column=0, columnspan=3,
            padx=5, pady=5,
            ipadx=3, ipady=4)


def clear_frame(shop, forest, desert, frame, progress, message):
    shop.config(state=NORMAL)
    forest.config(state=NORMAL)
    desert.config(state=NORMAL)

    progress.config(text=message)

    for widgets in frame.winfo_children():
        widgets.destroy()

#photo = ttk.PhotoImage(file="images/Hotpot.png")
#player_progress.config(image=photo)
welcome_note = ttk.Label(frame1,
                         text=Quotes.welcome_message,
                         #image=photo,
                         bootstyle="SUCCESS")
welcome_note.pack()


player_character = ttk.Label(frame1, text="", bootstyle="PRIMARY")
player_character.pack()


def chosenType():
    welcome_note.destroy()
    player_character.config(text="")
    alchemist_button.destroy()
    warrior_button.destroy()
    ninja_button.destroy()


def charChosen(char_attr_list):
    result = saveNewChar.saveChar(char_attr_list)
    if result:
        read_char_attr = open(f"{char_attr_list[0]}.txt", "r")
        player_character.config(text=read_char_attr.read())
        read_char_attr.close()

        start_game = ttk.Button(frame3,
                                text="Start Game",
                                command=lambda: startGame(char_attr_list[0],
                                                          player_character,
                                                          start_game),
                                bootstyle="LIGHT")
        start_game.pack()


def chooseWarrior():
    chosenType()
    char_attr_list = ["Warrior",
                      character_builds.warrior_strength,
                      character_builds.warrior_health,
                      character_builds.warrior_speed,
                      character_builds.warrior_intelligence,
                      character_builds.warrior_charisma]
    charChosen(char_attr_list)


def chooseNinja():
    chosenType()
    char_attr_list = ["Ninja",
                      character_builds.ninja_strength,
                      character_builds.ninja_health,
                      character_builds.ninja_speed,
                      character_builds.ninja_intelligence,
                      character_builds.ninja_charisma]
    charChosen(char_attr_list)


def chooseAlchemist():
    chosenType()
    char_attr_list = ["Alchemist",
                      character_builds.alchemist_strength,
                      character_builds.alchemist_health,
                      character_builds.alchemist_speed,
                      character_builds.alchemist_intelligence,
                      character_builds.alchemist_charisma]
    charChosen(char_attr_list)


warrior_button = ttk.Button(frame3,
                            text="Warrior",
                            command=chooseWarrior,
                            bootstyle="WARNING")
warrior_button.pack()

ninja_button = ttk.Button(frame3,
                          text="Ninja",
                          command=chooseNinja,
                          bootstyle="WARNING")
ninja_button.pack()

alchemist_button = ttk.Button(frame3,
                              text="Alchemist",
                              command=chooseAlchemist,
                              bootstyle="WARNING")
alchemist_button.pack()


def startGame(filename, player_character, start_game):

    player_character.destroy()
    start_game.destroy()

    player_type_text = open(f"{filename}.txt", "r")
    player_attr_lines = player_type_text.readlines()
    player_type_text.close()

    player_desc_text = ""
    for i in range(1, 6):
        player_desc_text += player_attr_lines[i]
    player_desc_text += player_attr_lines[10]
    player_desc = ttk.Label(frame2,
                            text=f"{filename}\n{player_desc_text}",
                            bootstyle="LIGHT")
    player_desc.pack()

    player_equipped_text = ""
    for i in range(6, 13):
        if i != 10:
            player_equipped_text += player_attr_lines[i]
    player_stuff = ttk.Label(frame4,
                             text=player_equipped_text,
                             bootstyle="LIGHT")
    player_stuff.pack()

    top_message = "Choose where you want to go"
    player_progress = ttk.Label(frame1,
                                text=f"\n{top_message}\n",
                                bootstyle="LIGHT")
    player_progress.pack()


    # Buttons to shop and go on 2x journeys
    go2shop = ttk.Button(frame3, text="Shop",
                         command=lambda: goShopping(buttonArguments))
    go2shop.pack()

    journey1 = ttk.Button(frame3, text="Forest",
                         command=lambda: forestJourney(buttonArguments))
    journey1.pack()

    journey2 = ttk.Button(frame3, text="Desert",
                         command=lambda: desertJourney(buttonArguments))
    journey2.pack()

    buttonArguments = [filename, player_stuff, go2shop,
                       journey1, journey2,
                       player_progress, player_desc]
    return


def buttonDisabler(shop, forest, desert):
    shop.config(state=DISABLED)
    forest.config(state=DISABLED)
    desert.config(state=DISABLED)
    pass


def forestJourney(buttonArguments):
    char_type = buttonArguments[0]
    player_stuff_label = buttonArguments[1]
    shop = buttonArguments[2]
    forest = buttonArguments[3]
    desert = buttonArguments[4]
    player_progress = buttonArguments[5]
    player_desc = buttonArguments[6]

    player_progress.config(text="You are in the forest")

    buttonDisabler(shop, forest, desert)

    stuff = [char_type, shop, forest, desert, frame5, player_progress, player_desc]

    runIntoForest = ttk.Button(frame5,
                       text="Run into the forest",
                       command=lambda: forestRun(stuff),
                       bootstyle="SUCCESS")
    runIntoForest.pack()

    walkIntoForest = ttk.Button(frame5,
                       text="Walk into the forest",
                       command=lambda: forestWalk(stuff),
                       bootstyle="SUCCESS")
    walkIntoForest.pack()

    exitForest = ttk.Button(frame5,
                       text="Leave the forest",
                       command=lambda: clear_frame(shop,
                                                   forest,
                                                   desert,
                                                   frame5,
                                                   player_progress,
                                                   "You left the forest"),
                       bootstyle="SUCCESS")
    exitForest.pack()

    def forestBattle(stuff, num_goblins):
        char_type = stuff[0]
        shop = stuff[1]
        forest = stuff[2]
        desert = stuff[3]
        frame5 = stuff[4]
        player_progress = stuff[5]
        player_desc = stuff[6]

        msg = f"You have encountered\n{num_goblins} Goblins!"
        player_progress.config(text=msg)

        for i in range(num_goblins):
            player_type_text = open(f"{char_type}.txt", "r")
            player_attr_lines = player_type_text.readlines()
            player_type_text.close()

            num_monsters_kill = player_attr_lines[10]
            num_monsters_killed = int(num_monsters_kill[-4:-1])

            time.sleep(1)
            result = battle.battle(char_type, num_monsters_killed)
            player_type_text = open(f"{char_type}.txt", "r")
            player_attr_lines = player_type_text.readlines()
            player_type_text.close()

            print(f"result ***{result}***")
            if result == "You died":
                player_progress.config(text=f"{msg} \nand Died")
                break

            elif result > 0:
                print(f"Sooooo.... \n{result} Goblins killed\n")
                player_attr_lines[10] = f"Monsters killed:   {result}\n"
                write_char_attr = open(f"{char_type}.txt", "w")
                for line in player_attr_lines:
                    write_char_attr.write(line)
                write_char_attr.close()

                player_desc_text = ""
                for i in range(1, 6):
                    player_desc_text += player_attr_lines[i]
                player_desc_text += player_attr_lines[10]

                player_desc.config(text=player_desc_text)
                player_progress.config(text=f"Well done\nYou survived the forest")
                pass

            else:
                pass
        pass


    def forestRun(stuff):
        num_monsters = random.randint(3,5)
        forestBattle(stuff, num_monsters)


    def forestWalk(stuff):
        num_monsters = random.randint(1,2)
        forestBattle(stuff, num_monsters)

    pass


def desertJourney(buttonArguments):
    char_type = buttonArguments[0]
    player_stuff_label = buttonArguments[1]
    shop = buttonArguments[2]
    forest = buttonArguments[3]
    desert = buttonArguments[4]
    player_progress = buttonArguments[5]
    player_desc = buttonArguments[6]

    player_progress.config(text="You are in the desert")

    buttonDisabler(shop, forest, desert)

    exitDesert = ttk.Button(frame5,
                       text="Leave the desert",
                       command=lambda: clear_frame(shop,
                                                   forest,
                                                   desert,
                                                   frame5,
                                                   player_progress,
                                                   "You left the desert"),
                       bootstyle="SUCCESS")
    exitDesert.pack()
    pass




# Create shop based on products listed in stuff file
# Making the check boxes and buy button

def goShopping(buttonArguments):

    char_type = buttonArguments[0]
    player_stuff_label = buttonArguments[1]
    shop = buttonArguments[2]
    forest = buttonArguments[3]
    desert = buttonArguments[4]
    player_progress = buttonArguments[5]

    #photo = ttk.PhotoImage(file="images/Hotpot.png")
    #player_progress.config(image=photo)

    buttonDisabler(shop, forest, desert)

    # Collecting information from stuff to populate values, to create checkboxes

    cb_texts = []
    cb_variables = []
    cb_onvalues = []

    for i, j in stuff.for_everyone.items():
        item_name, item_price = stuff.re_stuff_handler(i)
        available_item = f"\n{item_name}    {item_price}"
        stuff.for_everyone[i] = StringVar()

        cb_texts.append(available_item)
        cb_variables.append(stuff.for_everyone[i])
        cb_onvalues.append(i)

    if char_type == "Warrior":
        for i, j in stuff.warrior_stuff.items():
            item_name, item_price = stuff.re_stuff_handler(i)
            available_item = f"\n{item_name}    {item_price}"
            stuff.warrior_stuff[i] = StringVar()

            cb_texts.append(available_item)
            cb_variables.append(stuff.warrior_stuff[i])
            cb_onvalues.append(i)

    if char_type == "Ninja":
        for i, j in stuff.ninja_stuff.items():
            item_name, item_price = stuff.re_stuff_handler(i)
            available_item = f"\n{item_name}    {item_price}"
            stuff.ninja_stuff[i] = StringVar()

            cb_texts.append(available_item)
            cb_variables.append(stuff.ninja_stuff[i])
            cb_onvalues.append(i)

    if char_type == "Alchemist":
        for i, j in stuff.alchemist_stuff.items():
            item_name, item_price = stuff.re_stuff_handler(i)
            available_item = f"\n{item_name}    {item_price}"
            stuff.alchemist_stuff[i] = StringVar()

            cb_texts.append(available_item)
            cb_variables.append(stuff.alchemist_stuff[i])
            cb_onvalues.append(i)


    for i in range(len(cb_texts)):
        checkbox_for_item = ttk.Checkbutton(frame5,
                                    text=cb_texts[i],
                                    variable=cb_variables[i],
                                    onvalue=cb_onvalues[i],
                                    offvalue="",
                                    bootstyle="info-square-toggle")
        checkbox_for_item.pack()
        pass

    buyIt = ttk.Button(frame5,
                       text="Buy",
                       command=lambda: purchase(char_type),
                       bootstyle="SUCCESS")
    buyIt.pack()

    exitShop = ttk.Button(frame5,
                       text="Leave Shop",
                       command=lambda: clear_frame(shop,
                                                   forest,
                                                   desert,
                                                   frame5,
                                                   player_progress,
                                                   "You left the shop"),
                       bootstyle="SUCCESS")
    exitShop.pack()

    # Allow selected checkboxes to action trigger file updates when Buy is pressed
    def purchase(char_type):
        player_stats = open(f"{char_type}.txt", "r")
        player_attr_lines = player_stats.readlines()
        player_stats.close()

        coins_left = int(re.split("   ", player_attr_lines[6])[1])

        for item, justin in stuff.for_everyone.items():
            if stuff.for_everyone[item].get() != "":
                item_name, item_price = stuff.re_stuff_handler(item)
                update_file(char_type, coins_left, item_name, item_price)

        if char_type == "Warrior":
            for item, justin in stuff.warrior_stuff.items():
                if stuff.warrior_stuff[item].get() != "":
                    item_name, item_price = stuff.re_stuff_handler(item)
                    update_file(char_type, coins_left, item_name, item_price)

        if char_type == "Ninja":
            for item, justin in stuff.ninja_stuff.items():
                if stuff.ninja_stuff[item].get() != "":
                    item_name, item_price = stuff.re_stuff_handler(item)
                    update_file(char_type, coins_left, item_name, item_price)

        if char_type == "Alchemist":
            for item, justin in stuff.alchemist_stuff.items():
                if stuff.alchemist_stuff[item].get() != "":
                    item_name, item_price = stuff.re_stuff_handler(item)
                    update_file(char_type, coins_left, item_name, item_price)

    # Update char text file after a purchase is made
    def update_file(char_type, coins_left, item_name, item_price):

        if (coins_left - int(item_price)) < 0:
            print("Unable to purchase. Not enough coins")
            return False

        player_equipped_text = saveNewChar.shopPurchase(char_type, item_name, item_price, coins_left)
        player_stuff_label.config(text=player_equipped_text)
        return True


parent.mainloop()



