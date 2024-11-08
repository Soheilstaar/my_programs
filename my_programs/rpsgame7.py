# The rock,paper and scissors game with nested loops and recursive methods and function for optimizatio and using global variables and parent functions and modulation in order to play again and again and not having to restart the game using commands.


# Rock,Paper,Scissors game

import sys
import random
print("\n🔥✨🌟 Welcome to Rock,Paper and Scissors game 🔥✨🌟\n")

def rps():
    game_count=0
    player_wins=0
    python_wins=0

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

            
            def decide_winner(player,computer):
                nonlocal player_wins
                nonlocal python_wins
                if player == 1 and computer == 3:
                    player_wins +=1
                    return "You Win ! 🥳"
                elif player == 2 and computer == 1:
                    player_wins +=1
                    return "You Win ! 🥳"
                elif player == 3 and computer == 2:
                    player_wins +=1
                    return "You Win ! 🥳"
                elif player == computer:
                    return "Tie Game ! 😖"

                else:
                    python_wins +=1
                    return "Python Wins ! 🐍"
                
            game_result= decide_winner( player , computer)
            print(game_result)


            nonlocal game_count
            game_count += 1

            print('\nGame Count: ', str(game_count),'⏰')
            print('\nPlayer Wins: ', str(player_wins),'💃')
            print('\nPython Wins: ', str(python_wins),'🐍')

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
    return play_rps
        
rock_paper_scissors= rps()

if __name__ =='__main__':
    rock_paper_scissors()