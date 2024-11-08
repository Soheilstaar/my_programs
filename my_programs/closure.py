
def arcade(person,coins):
    def play_game():
        nonlocal coins
        coins -=1

        if coins > 1 :
            print('\n',person,' has ', str(coins),' Coins left.\n')
        elif coins==1:
            print('\n',person,' has ', str(coins),' Coin left.\n')
        else:
            print('\n',person,' is out of coins.\n')

    return play_game
Tommy = arcade('Tommy',3)
Jenny = arcade('Jenny',5)

Tommy()
Tommy()
Jenny()
Tommy()
Jenny()
Jenny()
Jenny()
Jenny()
Jenny()