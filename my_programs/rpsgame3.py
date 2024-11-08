# The rock,paper and scissors game with nested loops and recursive methods and function for optimizatio in order to play again and again and not having to restart the game using commands.


# Rock,Paper,Scissors game

import sys
import random
print("\n🔥✨🌟 Welcome to Rock,Paper and Scissors game 🔥✨🌟\n")

def play_rps():
    playagain = True

    while playagain:

        

        playerchoice = input ("Please make your choice:\n 1 for 🪨 \n 2 for 📜\n 3 for ✂️ \n\n")
        if playerchoice not in ['1','2','3']:
            print('Please enter 1,2 or 3')
            return play_rps()       
        player = int(float(playerchoice))
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("\nYou Chose", player, ".")
        print("Python Chose", computer, ".")
        print("")

        if player == 1 and computer == 3:
            print("You Win ! 🥳")
        elif player == 2 and computer == 1:
            print("You Win ! 🥳")
        elif player == 3 and computer == 2:
            print("You Win ! 🥳")
        elif player == computer:
            print("Tie Game ! 😖")

        else:
            print("Python Wins ! 🐍")

        print('\nPlay Again?')
        while True:
            playagain = input('\nY/N\n\n')
            if playagain.lower() not in ['y','n']:
                continue
            else:
                break
                
        if playagain.lower() == ('y'):
            return play_rps()
        else:
            print ('\n🔥✨🌟🔥\n Thank you for playing !\n✨🌟🔥✨🌟 ')
            sys.exit('\n Bye 👋\n\n')
    
play_rps()