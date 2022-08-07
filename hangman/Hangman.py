import random
import string
from Words import words



def get_word():
    word = words[random.randint(0, len(words))]
    if " " or "-" in words:
        word = words[random.randint(0, len(words))]
    return word

def play():
    lives = 10
    word = "test"  # change this back to get_word()
    used_letters = set()
    letters_left = set(word)
    correct_letters = [letter if letter in used_letters else "-" for letter in word]
    while lives > 0 and len(letters_left)>0:
        print("You have {} lives left!".format(lives))
        print("Used letters: ", " ".join(used_letters))
        print("Correct Word = ", " ".join(correct_letters))  # have to add missing letters
        guess = input("lets play Hangman: Guess a letter: ").lower()
        if guess not in string.ascii_lowercase:
          print("Invalid Entry")
          play()
        elif guess in word:
            if guess in used_letters:
                print("You already guessed that letter!")
            else:
                print("Correct!")
                used_letters.add(guess)
                letters_left.remove(guess)
                print(" ")
        else:
            print("Sorry incorrect!")
            used_letters.add(guess)
            lives = lives - 1
    print("Congrats you win. The word was {}".format(word))

play()
