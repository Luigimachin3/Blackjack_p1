from p1_random import P1Random

# Initialize random number outside the loop
rng = P1Random()

# Set initial values for game variables
game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
tie_games = 0


# Function that prints a message based on the value of the card number.
# Updates the card number to its value
def card_legend(card_value):
    if card_value == 1:
        print("Your card is a ACE!")
        card_value = 1
    elif 2 <= card_value <= 10:
        print(f"Your card is a {card_value}!")
    elif card_value == 11:
        print("Your card is a JACK!")
        card_value = 10
    elif card_value == 12:
        print("Your card is a QUEEN!")
        card_value = 10
    elif card_value == 13:
        print("Your card is a KING!")
        card_value = 10
    return card_value


# Control the number of games the player will play
while game_continue:  # game #1, #2, #3
    # 1. Print game number message and updated each time a game is played
    game_num += 1
    print(f"START GAME #{game_num}\n")

    # 2. Deal a card to the player automatically
    player_hand = 0
    card = rng.next_int(13) + 1
    card = card_legend(card)

    # 3. Add card number to the player's hand value
    player_hand += card

    # 4. Print player's hand value
    print(f"Your hand is: {player_hand}\n")

    # 5. Inner loop to keep playing the current game by prompting the player to choose a menu option
    no_winner = True
    while no_winner:
        # Print four menu options
        print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")

        # Prompt player for an input to choose a menu option
        option = int(input("Choose an option: "))
        print()

        # Deal another card to the player if option 1 is selected
        if option == 1:
            # deal another card to the player
            card = rng.next_int(13) + 1
            card = card_legend(card)
            # calculate the player's hand value
            player_hand += card
            print(f"Your hand is: {player_hand}\n")

            # Check if player has 21 or exceeded 21, and determine the winner
            if player_hand == 21:
                print("BLACKJACK! You win!\n")
                player_wins += 1
                no_winner = False
            elif player_hand > 21:
                print("You exceeded 21! You lose.\n")
                dealer_wins += 1
                # Update the number of games player/dealer wins
                no_winner = False

        # Compare player and dealer hands if option 2 is selected
        elif option == 2:
            # 1. Deal a card to the dealer
            dealer_hand = rng.next_int(11) + 16
            # 2. Compare player hand value with dealer hand value
            print(f"Dealer's hand: {dealer_hand}\nYour hand is: {player_hand}\n")
            # 3. And determine who wins the game
            if dealer_hand > 21:
                print("You win!\n")
                player_wins += 1
            elif dealer_hand == player_hand:
                print("It's a tie! No one wins!\n")
                tie_games += 1
            elif dealer_hand > player_hand:
                print("Dealer wins!\n")
                dealer_wins += 1
            else:
                print("You win!\n")
                player_wins += 1

            # 4. Update number of games player/dealer wins
            no_winner = False

        # Print the statistics of the game if option 3 is selected
        elif option == 3:
            print(f"Number of Player wins: {player_wins}\n"
                  f"Number of Dealer wins: {dealer_wins}\n"
                  f"Number of tie games: {tie_games}\n"
                  f"Total # of games played is: {game_num - 1}")
            if game_num != 1:
                print(f"Percentage of Player wins: {(player_wins / (game_num - 1)) * 100:.1f}%\n")
            else:
                print(f"Percentage of Player wins: {player_wins / game_num * 100:.1f}%\n")

        elif option == 4:
            no_winner = False  # Get outside the inner while
            game_continue = False  # Get outside the outer while
        else:  # Print invalid message
            print("Invalid input!\nPlease enter an integer value between 1 and 4.\n")
