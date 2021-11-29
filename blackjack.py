from random import choice

player1 = []
dealer = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def player_deal():
    player1.append(choice(cards))
    player1.append(choice(cards))

def dealer_deal():
    dealer.append(choice(cards))

def hit():
    return player1.append(choice(cards))
    

def blackjack():
    game_over = False
    while game_over == False:
        choice = input(f"Your hand is {player1}. Would you like to (h)it or (s)tay? " )
        if choice in ("h", "hit"):
            hit()
            print(f"You now have {player1} for a total of {sum(player1)}.")
            if sum(player1) > 21:
                print("You lose!")
                game_over = True
            elif sum(player1) < 21:
                blackjack()
        elif choice in ("s", "stay"):
            print(f"You have {player1} for a total of {sum(player1)}.")
            while sum(dealer) < 17:
                dealer_deal()
            print(f"The dealer has {dealer} for a total of {sum(dealer)}.")
            if sum(player1) > sum(dealer) and sum(player1) <= 21:
                print(f"You have {player1} with a total of {sum(player1)}.\n The dealer has {dealer} with a total of {sum(dealer)}. You win!")
                game_over = True
            if sum(player1) < sum(dealer) and sum(dealer) <= 21:
                print(f"You have {player1} with a total of {sum(player1)}.\n The dealer has {dealer} with a total of {sum(dealer)}. You lose.")
                game_over = True
            elif sum(player1) > 21:
                print(f"You bust with {player1} for a total of {sum(player1)}.")
                game_over = True
            elif sum(dealer) > 21:
                print(f"The dealer busts with a total of {sum(dealer)}. You win!")
                game_over = True
            elif sum(dealer) == sum(player1):
                print("It's a draw.")
                game_over = True

player_deal()
dealer_deal()
blackjack()
