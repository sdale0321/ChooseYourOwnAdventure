name = input("Type your name: ")
print("Well hoinky doinky, welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around or try to swim across.  Type walk to walk around or type swim to try to swim across: ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid optoin. You lose.")

elif answer == "right": 
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and loseeeeee.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stranger, they give you gold.  You win!")
        elif answer == "no":
            print("You ignore the stranger and they wait til you walk by to jump you.  You lose.")
        else:
            print("Not a valid optoin. You lose.")
    else:
        print("Not a valid optoin. You lose.")
else:
    print('Not a valid option. You lose.')