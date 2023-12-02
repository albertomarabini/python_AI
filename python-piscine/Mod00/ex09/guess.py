import random

def guessing_game():
    secret_number = random.randint(1, 99)
    attempts = 0

    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game. Good luck!")

    while True:
        user_input = input("What's your guess between 1 and 99?\n>> ")
        attempts += 1

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            guess = int(user_input)
        except ValueError:
            print("That's not a number.")
            continue

        if guess < 1 or guess > 99:
            print("Out of bounds. Please try again.")
            continue

        if guess == secret_number:
            if secret_number == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if attempts == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print(f"Congratulations, you've got it!\nYou won in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

if __name__ == "__main__":
    guessing_game()
