import random
from replit import clear
from art import logo

number = random.randint(1,100)

def game():
  """Function to ask the user for a guess and compare it with a random number informing the user if its guess was too high or too low. """
  user_guess = int(input("Make a guess between 1 and 100: "))
  if user_guess != number:
    if user_guess > number:
      print("Too high.")
    elif user_guess < number:
      print("Too low")
  else:
    print(f'You got it! The number was {number}')
    play_game()

def game_attempts():
  """Function to let the user choose the game difficulty and inform the remaining attempts."""
  print(logo)
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    guesses = 10
    while guesses > 0:
      game()
      guesses -= 1
      print (f'You have {guesses} attempts remaining to guess the number.')
  elif difficulty == "hard":
    guesses = 5
    while guesses > 0:
      game()
      guesses -= 1
      print (f'You have {guesses} attempts remaining to guess the number.')
    if guesses == 0:
      print("You've run out of guesses, you lose!")
  else:
    print("Please type 'easy' or 'hard'")

def play_game():  
  """Function to ask the user to play the guessing game and to clear the screen for each new game."""
  while input("\nDo you want to play Guess The Number? Type 'yes' or 'no': ").lower() == "yes":
    clear()
    game_attempts()
  else:
    print("Thank you for playing!")

play_game()