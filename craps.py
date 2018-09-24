#Basic craps game

from random import randint

def main():
    print("Rolling dice...")

    dice1 = randint(1,6)
    print("Dice 1: ", dice1)
    dice2 = randint(1,6)
    print("Dice 2: ", dice2)
    dice_roll = int(dice1+dice2)
    print("Total of the dice roll: ", dice_roll)
    play_game(dice_roll)

def play_game(dice_roll):
    isPlay = True
    if(dice_roll==7 or dice_roll==11):
        print("You win!")
        play_again = int(input("Press 1 if you want to play again, Press anything else if you want to exit: "))
        if(play_again==1):
            main()
        else:
            print("Thanks for playing!")
    elif(dice_roll==2 or dice_roll==3 or dice_roll==12):
        print("You lose!")
        play_again = int(input("Press 1 if you want to play again, Press anything else if you want to exit: "))
        if(play_again==1):
            main()
        else:
            print("Thanks for playing!")
    else:
        print(dice_roll, " is the point! Keep rolling...")

        while(isPlay==True):
            dice1 = randint(1,6)
            print("Dice 1: ", dice1)
            dice2 = randint(1,6)
            print("Dice 2: ", dice2)
            dice_roll2 = int(dice1+dice2)
            print("Total of the dice roll: ", dice_roll2)
            if(dice_roll2 == 7):
                print("You lose!")
                play_again = int(input("Press 1 if you want to play again, Press anything else if you want to exit: "))
                if(play_again==1):
                    main()
                else:
                    print("Thanks for playing!")
                isPlay=False
            elif(dice_roll2==dice_roll):
                print("You win!")
                play_again = int(input("Press 1 if you want to play again, Press anything else if you want to exit: "))
                if(play_again==1):
                    main()
                else:
                    print("Thanks for playing!")
                isPlay=False
            else:
                isPlay=True

main()
