import random


def guess_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Максимум 10 попыток

    while attempts < max_attempts:
        # какой-то комментарий
        # ещё один комментарий
        # последний комментарий
    while True:
        # Какой-то комментарий

        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")


    if attempts >= max_attempts:
        print(f"Sorry, you've reached the maximum attempts. The number was {number_to_guess}.")


if __name__ == "__main__":
    guess_number()

