import random
from art import logo, vs
from game_data import data
from replit import clear

print(logo)


def random_person():
	""" Function to select a random person from a list.
  Return: the random choice
  """
	return random.choice(data)


def data_format(person):
	""" Function to takes the data and return it into a printable format.
  Return: name, description and country.
  """
	name = person['name']
	description = person['description']
	country = person['country']
	return f'{name}, {description}, from {country}'


def compare_followers(person_A, person_B, choice):
	"""Function to compare the followers from person A and person B with the user choice.
  """
	if person_A['follower_count'] > person_B['follower_count']:
		return choice == "A"
	else:
		return choice == "B"


def main():
	score = 0
	keep_playing = True
	person_B = random_person()
	while keep_playing:
		person_A = person_B
		person_B = random_person()
		if person_A == person_B:
			person_B = random_person()
		print(f'Compare A: {data_format(person_A)}.')
		print(vs)
		print(f'Against B: {data_format(person_B)}.')
		user_choice = input(
		    "Who has more followers? Type 'A' or 'B': ").upper()
		is_correct = compare_followers(person_A, person_B, user_choice)
		clear()
		print(logo)
		if is_correct:
			score += 1
			print(f"You're right! Current score: {score}")
		else:
			keep_playing = False
			print(f"You're wrong. Final score {score}")


if __name__ == "__main__":
	main()
