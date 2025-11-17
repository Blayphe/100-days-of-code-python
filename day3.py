print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a = input("You have begun wandering through the jungle, with a machete in hand you clear a path but discover two "
          "directions. The left leads to a damp and dark cave, the right leads to a denser part of the jungle. Which "
          "way will you go (Type left or right)?: ").lower()
if a == "left":
    b = input("You process left towards the cave, at the entrance you find a lantern and adventure deep "
              "within. "
              "You are not "
              "alone, you see a wild bear sleeping ahead. Do you sneak past it or attack (Type sneak or "
              "attack)?: ").lower()
    if b == "sneak":
        print("Holding your breathe, you sneak past the snoozing bear being as quiet as possible and successful! "
              "What's that sound? It is glistening golden treasure you can sense it nearby!")
        c = input("Your final trial awaits as you come across 3 animals, one will guide you to riches, the others to a "
                  "grim fate. Choose wisely between the penguin, cheetah, and zebra (Type penguin, cheetah, "
                  "or zebra): ").lower()
        if c == "cheetah":
            print("You choose the cheetah for its vibrant spots, the other two animals disappear within an instant. "
                  "The cheetah growls beckoning you to follow, but as you begin to walk your legs feel heavy. You "
                  "pass out and the cheetah devours you, Game over.")
        elif c == "zebra":
            print("You choose the zebra for its pretty pattern, however as the other 2 animals vanish you begin to "
                  "fall under a deep trance staring at the zebra. In no time you collapse never to awaken again, "
                  "Game over.")
        elif c == "penguin":
            print("You choose the penguin because after all it is the best animal, it waddles over to you and gives "
                  "you a hug before leading you to a room filled with a mountain of golden treasure! Gems, Jewelry, "
                  "and golden coins fill the room as you bask in the glory.")
            print(r'''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
            |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
            ''')
        else:
            print("Skill dif you typed wrong, Game over.")

    else:
        print("You attack the bear with all your might! However it gets the best of you and tears you to shreds "
              "enjoying you for dinner, Game Over.")

else:
    print("You delve deeper however the jungle becomes too dense and you become trapped lost forever, Game Over.")
