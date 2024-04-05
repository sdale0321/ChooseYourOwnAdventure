name = input("Type your name: ")
print("Well hoinky doinky, welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go?").lower()
#by setting answer to input, it allows us to play this game of nesting loops 
if answer == "left":
    answer = input("You come to a river, you can walk around or try to swim across.  Type walk to walk around or type swim to try to swim across: ").lower()
    #by setting the condition for the users answer to match one of two words (for now), we can determine a "path" that the user wants to take.  
    #Once that path is determined you can set the variable "answer" to yet another question to determine the next path.
    if answer == "swim": #nesting the next set of if/elif/else statements within the first is what allows the users path to progress down multiple outcomes.  
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose.")

elif answer == "right": #part of the larger if/elif/else set of loops encapsulating the sub-paths a user can take.  
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
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.") #this is a shorter example of this concept and can be added onto 
else:
    print('Not a valid option. You lose.')
print("Thank you for trying")
