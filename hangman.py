import random

# List of words for the game
words = ["apple", "banana", "cherry", "dog", "elephant", "frog", "grape", "hamburger", "internet", "jazz"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play the Hangman game
def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # You can customize the number of attempts

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
            current_display = display_word(word_to_guess, guessed_letters)
            print(current_display)

            if current_display == word_to_guess:
                print("Congratulations, you've won! The word was:", word_to_guess)
                break
        else:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts remaining.")
    else:
        print("You've run out of attempts. The word was:", word_to_guess)

# Start the game
play_hangman()
