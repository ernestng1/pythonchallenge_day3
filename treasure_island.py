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
''') #add the ''' so that you can keep the different parts of the ASCII in the different lines
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input('You\'re a a sandy beach, would you like to turn "left"(l) or "right"(r)?\n').lower()  #lower to make user's input lowercase
if left_or_right == "l":
    print("You headed towards a tropical forest and you see a murky lake")
    swim_or_wait = input('Would you like to "swim"(s) across the lake or "wait"(w) for a boat?\n').lower()
    if swim_or_wait == "w":
        print("The boat arrived and you reach a small island with three visible doors, "
              "once of which seems to be where the treasure chest is!")
        door =  input('Which door would you enter through? The "Red"(r), "Yellow"(y) or "Blue"(b) door?\n').lower()
        if door == "r":
            print("You got burned by fire. Game Over!")
        elif door == "b":
            print("You got eaten by beasts waiting for you behind the blue door. Game Over!")
        elif door == "y":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("You got attacked by trout. Game Over.")
else:
    print("You fall over a hole. Game Over!")