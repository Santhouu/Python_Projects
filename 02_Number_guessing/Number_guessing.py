import random
#importing the some pre-defined libraries 

def number_guessing_game():
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    print("I have chosen a random number between 1 and 100.")
    print("Your task is to guess it with as few attempts as possible. Good luck!")

    # Generate a random number
    # Generate a random number between 1 and 100 for the game

    secret_number = random.randint(1, 100)
    attempts = 0  # To count the number of attempts

    # Add range hints
    low, high = 1, 100

    while True:
        try:
            # Show the guessing range
            print(f"\nHint: The number is between {low} and {high}.")

            # Take user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Validate the guess
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100.")
                continue

            # Check the guess
            if guess < secret_number:
                print("📉 Too low!")
                low = max(low, guess + 1)  # Narrow the lower range
            elif guess > secret_number:
                print("📈 Too high!")
                high = min(high, guess - 1)  # Narrow the upper range
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    # Offer replay option
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay in ("yes", "y"):
        number_guessing_game()
    else:
        print("Thank you for playing! See you next time. 😊")


# Run the game
if __name__ == "__main__":
    number_guessing_game()