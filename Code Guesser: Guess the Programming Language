import random

def choose_language():
    languages = ["python", "java", "kotlin", "swift", "r", "javascript", "ruby"]
    return random.choice(languages)

def display_word(language, guessed_letters):
    display = ""
    for letter in language:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        display += " "
    return display.strip()

def hangman():
    while True:
        language = choose_language()
        guessed_letters = []
        attempts = 6

        print("\nWelcome to Code Guesser: Guess the Programming Language: ")
        print("I've chosen a programming language. Can you guess what it is?")
        print("You have", attempts, "attempts to guess the language.")

        while attempts > 0:
            print("\nLanguage:", display_word(language, guessed_letters))

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess not in language:
                print("Incorrect guess! Try again.")
                attempts -= 1
            else:
                print("Correct guess!")

            if all(letter in guessed_letters for letter in language):
                print("Congratulations! You guessed the programming language:", language)
                break

            print("Attempts left:", attempts)

        if attempts == 0:
            print("Sorry, you ran out of attempts! The programming language was:", language)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
hangman()
