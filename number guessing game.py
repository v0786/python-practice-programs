import random

# Set the range for the random number
min_number = 1
max_number = 10
secret_number = random.randint(min_number, max_number)

# Set the number of guesses allowed
max_attempts = 3
attempts = 0

print("Welcome to the Number Guessing Game!")
print(f"Guess the number between {min_number} and {max_number}.")

while attempts < max_attempts:
    try:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        
        # Increase the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

        # Inform the player about the remaining attempts
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts remaining.")
        else:
            print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Thank you for playing!")
