from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")

users_bids = {}
other_bidders = True

def final_winner (total_bids):
  high_bid = 0
  winner = ""
  for user in total_bids:
    bid_amount = total_bids[user]
    if bid_amount > high_bid:
      high_bid = bid_amount
      winner = user
  print(f'The winner is {winner} with a bid of ${high_bid}.')
      
while other_bidders:
  name = input("What is your name? ")
  bid = int(input("What\'s your bid? $"))
  users_bids[name] = bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  clear()
  if more_bidders == "no":
    other_bidders = False
    final_winner(users_bids)

