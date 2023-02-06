import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the correct word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #letters the user has already guessed
    lives = 10
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left.")
        print("You have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ","".join(word_list))
        guess = input("Guess a letter.").upper()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1
        elif guess in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please guess an alphabet from A to Z")
    if len(word_letters) == 0:
        print(f"Congratulations! You guessed the word {word}!")
    else:
        print(f"Sorry, you lost. The word was {word}.")





hangman()
