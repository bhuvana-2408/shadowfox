import random

words = {
    "python": "A popular programming language",
    "github": "A platform for storing code",
    "coding": "What programmers do",
    "hangman": "The game you are building",
    "developer": "A person who writes software"
}

secret_word = random.choice(list(words.keys()))
hint = words[secret_word]

guessed_word = ["_"] * len(secret_word)
attempts = 6

print("Welcome to Hangman!")
print("Hint:", hint)

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame Over!")
    print("The word was:", secret_word)