import random #imports the random module in py

def get_starting_balance():
    """
    Greets the player and assigns a random starting balance.
    """
    name = input("Good evening, may I have your name? ")

    balance = random.randrange(1000, 20000)

    print("\n--------------------------------------------------")
    print(f"Welcome, Mr/Ms {name}.")
    print(f"Your starting balance has been allocated: ${balance}")
    print("Let us begin the game.\n")
    print("--------------------------------------------------")

    return name, balance


def get_bet_amount(balance):
    """
    Prompts the user for a valid bet amount.
    """
    while True:
        try:
            bet = int(input(f"Kindly enter your wager (Available balance: ${balance}): $"))

            if bet > balance:
                print("Apologies, you cannot wager more than your available balance.")
            elif bet <= 0:
                print("The wager must be greater than $0.")
            else:
                return bet

        except ValueError:
            print("Please enter a valid numerical value.")


def get_dice_guess():
    """
    Asks the player to guess a dice number between 1 and 6.
    """
    while True:
        try:
            guess = int(input("Predict the dice outcome (choose a number between 1 and 6): "))

            if 1 <= guess <= 6:
                return guess
            else:
                print("Kindly select a number between 1 and 6.")

        except ValueError:
            print("Invalid entry. Please enter a number between 1 and 6.")


def play_round(balance):
    """
    Executes one round of the dice betting game.
    """
    bet = get_bet_amount(balance)
    guess = get_dice_guess()

    dice = random.randint(1, 6)

    print(f"\nThe dice has been rolled... 🎲")
    print(f"Result: {dice}")

    if guess == dice:
        print("Splendid! Your prediction was correct.")
        print("You receive double your wager.")
        balance += bet
        win = True
    else:
        print("Unfortunate. Your prediction was incorrect.")
        print("Your wager has been deducted.")
        balance -= bet
        win = False

    print(f"Updated balance: ${balance}\n")

    return balance, win


def offer_loan(balance, loan_taken):
    """
    Offers a one-time loan if the player loses all funds.
    """
    if balance > 0 or loan_taken:
        return balance, loan_taken

    print("\nYou currently possess no remaining funds.")

    choice = input("Would you like to take a loan to continue playing? (y/n): ").lower()

    if choice == 'y':
        try:
            loan = int(input("Enter desired loan amount ($100 - $1500): "))

            if 100 <= loan <= 1500:
                balance += loan
                loan_taken = True
                print(f"A loan of ${loan} has been granted. Please use it wisely.\n")
            else:
                print("Loan request denied: amount outside permitted range.")

        except ValueError:
            print("Invalid amount entered.")

    return balance, loan_taken


def main():
    """
    Main game loop.
    """

    name, balance = get_starting_balance()

    wins = 0
    losses = 0
    rounds = 0
    loan_taken = False

    while True:

        if balance <= 0:
            balance, loan_taken = offer_loan(balance, loan_taken)

            if balance <= 0:
                print("\nYou no longer possess sufficient funds to continue.")
                break

        balance, win = play_round(balance)

        rounds += 1

        if win:
            wins += 1
        else:
            losses += 1

        choice = input("Would you care to play another round? (y/n): ").lower()

        if choice != 'y':
            break

    print("\n=================================================")
    print("Game Summary")
    print("=================================================")
    print(f"Player: {name}")
    print(f"Rounds Played: {rounds}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Final Balance: ${balance}")
    print("Thank you for participating. Farewell.")
    print("=================================================")


if __name__ == "__main__":
    main()
