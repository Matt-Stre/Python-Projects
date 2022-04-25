import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from list
    while '-' in word or ' ' in word:
        word=random.choice(words) # prevents irregular characters in the word

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed

    lives = 10

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # used letters
        print('You have ' +str(lives)+ ' lives and have used these letters: ', ' '.join(used_letters))

        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ''.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print('Wrong letter')

        elif user_letter in used_letters:
            print("You already used that character. Guess a new character")

        else:
            print("Invalid character.")

    #gets here when guessed word or out of lvies
    if lives == 0:
        print('You ran out of lives. You lose. The word was ' +word+ '!')
    else:
        print('You Win! You have guessed the word ' +word+ '!')

hangman()
