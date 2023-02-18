""""
ACIT2515 Lab
Aline Hammermuller
"""
import random

# The number of turns allowed is a global constant
NB_TURNS = 10

def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    with open ("words.txt", "r") as file:
        f1 = file.readlines()
        selected_word = random.choice(f1)
    return selected_word.strip()

def show_letters_in_word(word, letters):
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).

    DO NOT USE PRINT!

    Example:
    >>> show_letters_in_word("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> show_letters_in_word("TIM", ["G", "V"])
    '_ _ _'
    >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    char_list = []
    word = word.upper()
    letters = [letter.upper() for letter in letters]
    for char in word:    
        if char in letters:
            char_list.append(char)
        else:
            char_list.append('_')
    return ' '.join(char_list)

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
    return "_" not in show_letters_in_word(word,letters)

    
def main(turns):
    """
    Runs the game. Allows for "turns" loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of letters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the show_letters_in_word function to display hints about the word
    5. Remove 1 to the number of tries left
    6. Check if the player
        - won (= word has been found)
        - lost (= word has not been found, no tries left)

    Do not forget to pick a random word first :-)

    """
    word = pick_random_word().upper()
    letters_list = []
    end_of_game = False

    while not end_of_game:
        guess = input("Please enter a letter: ").upper()
        print(guess)
        if guess in letters_list or guess == "":
            print(f"You already tried this letter {guess}")
        letters_list.append(guess)
        print(show_letters_in_word(word, letters_list))
        if guess not in word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

        turns -= 1
        print(f'Turns remaining: {turns}')
        if turns == 0:
            end_of_game = True
            print("You lost.")
            print(f'Pssst, the solution was {word}.')

        if all_letters_found(word, letters_list):
            print("You win")
            end_of_game = True


if __name__ == "__main__":
    main(NB_TURNS)
