#Rock,Paper,Scissors game

import sys
import random

print('🔥✨🌟 Welcome to Rock,Paper and Scissors game 🔥✨🌟')

playerchoice =input('Please make your choice:\n 1 for 🪨 \n 2 for 📜\n 3 for ✂️\n\n')
print('')
player = int(float(playerchoice))
if player < 1 or player > 3:
    sys.exit('Please enter 1,2 or 3')

computerchoice = random.choice('123')
computer = int(computerchoice)
        
print('You Chose', player, ".")
print('Python Chose', computer ,".")
print('')

if player == 1 and computer == 3:
    print('You Win ! 🥳')
elif player == 2 and computer == 1:
    print('You Win ! 🥳')
elif player == 3 and computer == 2:
    print('You Win ! 🥳')
elif player == computer:
    print('Tie Game ! 😖')

else:
    print('Python Wins ! 🐍')