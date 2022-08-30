import random
from replit import clear
from art import logo

def cards_selection():
  """Returns a random card from a list of cards."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card
  
def score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare_score(user_score, computer_score):
  if computer_score == user_score:
    return "It's a draw."
  elif computer_score == 0:
    return "You lose. The computer has a Blackjack!"
  elif user_score == 0:
    return "Congratulations! You win! You have a Blackjack!"
  elif user_score > 21:
    return "You lose. You have more than 21 points."
  elif computer_score > 21:
    return "You win! the computer has more than 21 points."
  elif user_score > computer_score:
    return "You win! Your score is bigger than the computer score."
  else:
    return "You lose. Your score is lower than the computer score."

def play_game():
  print(logo)
  computer_cards = []
  user_cards = []
  keep_playing = True
  
  for card in range(0,2):
    computer_cards.append(cards_selection())
    user_cards.append(cards_selection())
  
  while keep_playing:
    user_score = score(user_cards)
    computer_score = score(computer_cards)
    print(f'Your cards {user_cards} and your score {user_score}')
    print(f'Computer\'s first card: {computer_cards[0]}')
    
    if 0 == user_score > 21 or 0 == computer_score > 21:
      keep_playing = False
    else:
      another_card = input("Type 'y' to get another card or 'n' to pass: ").lower()
      if another_card == 'y':
        user_cards.append(cards_selection())
      else:
        keep_playing = False
  
  while 17> computer_score !=0:
    computer_cards.append(cards_selection())
    computer_score = score(computer_cards)
  
  print(f'\nYour final hand: {user_cards} and your final score: {user_score}')
  print(f'Computer final hand: {computer_cards} and computer final score: {computer_score}')
  print(compare_score(user_score, computer_score))

while input("\nDo you want to play Blackjack? Type 'y' or 'n': ").lower() == 'y':
  clear()
  play_game()
  