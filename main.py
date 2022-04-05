answer = input("Would you like to play? (yes/no)")

if answer.lower().strip() == "yes":
    answer = input("You reach a crossroad. Would you like to go left or right? (left/right)").lower().strip()
    if answer == "left":
        answer = input("You encounter a bandit! What will you do? (attack/run)")
        if answer == "attack":
            print("You attacked! Did 5 damage to the bandit! The Bandit fell into the river!")
            print("Game Over! (Best Ending!)")
        elif answer == "run":
            print("You ran away from the bandit!")
            print("Game Over! (Neutral Ending!)")
        else:
            print("Uh oh! That was a bad decision! Bandit attacks you! Does 25 Damage! You fainted!")
            print("Game Over! (Worst Ending!!!)")
    elif answer == "right":
        print("You end up running into the vast woods! Will you survive?")
        print("To be continued!!!")
    else:
        print("Invalid Choice! Game Over!")
else:
    print("That's too bad!")