# Aline Hammermuller
# A01276569
import random


class SecretWord:

    def __init__(self, word = None):
        if word == None:
            with open ("words.txt", "r") as file:
                f1 = file.readlines()
                selected_word = random.choice(f1)
                self.word = selected_word.strip().upper()
        else:
            self.word = word.upper()

    
    def show_letters(self, letters):
        char_list = []
        self.letters = [letter.upper() for letter in letters]
        
        for char in self.word:  
            if char in letters:
                char_list.append(char)
            else:
                char_list.append('_')
        return ' '.join(char_list)

    def check_letters(self, letters):
        return "_" not in self.show_letters(letters)
    
    def check(self, string):
        return string.upper() == self.word


class Game:

    def __init__(self, turns=10):
        self.turns = turns
        self.letters_list = []
        self.secret_word = SecretWord()

    def play_one_round(self):
        guess = input("Please enter a letter: ").upper()

        while guess in self.letters_list:
            guess = input("You already tried this letter {guess}. Please enter a letter: ").upper()

        while len(guess) == 0:
            guess = input("You already tried this letter {guess}. Please enter a letter: ").upper()

        if len(guess) == 1:
            self.turns -= 1
            self.letters_list.append(guess)
            print(self.secret_word.show_letters(self.letters_list))
            print(f'Turns remaining: {self.turns}')
            return self.secret_word.check_letters(self.letters_list)

        if guess == self.secret_word or len(guess) > 1:
            print(self.secret_word.show_letters(self.letters_list))
            self.turns -= 1
            print(f'Turns remaining: {self.turns}')
            return self.secret_word.check(guess)

    def play(self):
        end_of_game = False
        while not end_of_game:
            if self.play_one_round() == True:
                print("You won")
                end_of_game = True
                return True
            elif self.turns == 0:
                end_of_game = True
                print("You lost.")
                print(f'Pssst, the solution was {self.secret_word.word}.')
                return False
