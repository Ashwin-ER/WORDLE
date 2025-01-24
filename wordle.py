import random

# List of 5-letter words (you can expand this list)
WORDS = [
    "apple", "brave", "crane", "dwarf", "eagle", "flame", "grape", "honey", "igloo", "jolly",
    "karma", "lemon", "mango", "noble", "olive", "pearl", "quilt", "robin", "sugar", "tiger",
    "umbra", "vivid", "whale", "xenon", "yacht", "zebra"
]

def choose_word():
    """Select a random word from the list."""
    return random.choice(WORDS)

def validate_guess(guess):
    """Ensure the guess is a valid 5-letter word."""
    return len(guess) == 5 and guess.isalpha()

def check_guess(secret_word, guess):
    """Compare the guess to the secret word and provide feedback."""
    feedback = []
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append("🟩")  # Correct letter in the correct position
        elif guess[i] in secret_word:
            feedback.append("🟨")  # Correct letter in the wrong position
        else:
            feedback.append("⬛")  # Letter not in the word
    return feedback

def display_feedback(feedback):
    """Display the feedback in a user-friendly format."""
    print(" ".join(feedback))

def wordle():
    """Main function to run the Wordle game."""
    secret_word = choose_word()
    attempts = 6

    print("Welcome to Wordle!")
    print("You have 6 attempts to guess the 5-letter word.")
    print("Feedback:")
    print("🟩 = Correct letter in the correct position")
    print("🟨 = Correct letter in the wrong position")
    print("⬛ = Letter not in the word")

    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt}:")
        while True:
            guess = input("Enter your guess: ").lower()
            if validate_guess(guess):
                break
            else:
                print("Invalid guess. Please enter a 5-letter word.")

        feedback = check_guess(secret_word, guess)
        display_feedback(feedback)

        if guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' in {attempt} attempts!")
            return

    print(f"\nGame over! The secret word was '{secret_word}'.")

# Run the game
if __name__ == "__main__":
    wordle()
