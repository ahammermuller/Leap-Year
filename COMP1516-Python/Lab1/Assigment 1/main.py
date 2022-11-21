

import assignment1

"""
It also has a main function which has a few instructions, loops, and nested loops as follows: 
it calls print_json_countries_and_capitals(), 
then prints get_list_of_countries_whose_nth_letter_is(n, letter) inside nested loops where 
n ranges from 1 to 3 and letter ranges from the elements in [‘a’, ‘e’, ‘i’, ‘o’, ‘u’] (for a total of 15 loops). 
Then it prints get_funny_case_capital_cities(letter) for each letter of the alphabet, 
and then print get_doubled_letter_countries().
"""


def main():
    assignment1.print_json_countries_and_capitals()
    print(assignment1.get_list_of_countries_whose_nth_letter_is(3, "M"))
    print(assignment1.get_funny_case_capital_cities("u"))
    print(assignment1.get_doubled_letter_countries())


if __name__ == '__main__':
    main()
