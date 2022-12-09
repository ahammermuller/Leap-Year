# Aline Hammermuller
# A01276569

from data import capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    """
    Function to check if the name of a file is valid and write all the countries and capitals from a
     dictionary in this file.
    :param filename:
    """
    file_name_pattern = "^[a-zA-Z0-9]{1,8}.txt$"
    while True:
        if re.search(file_name_pattern, filename):
            with open(filename, "w") as file:
                for country, capital in countries_capitals_dictionary.items():
                    file.write(f'The capital of {country} is {capital}.\n')
                break
        else:
            filename = input("Invalid filename. Please enter another filename ")


def save_capitals():
    """
    Function to check which capitals from a tuple matches a patters and write it in specific text files.
    """
    vowel_pattern = "[aeiou]{3}"
    cons_pattern = "[bcdfghjklmnpqrstwxyz]{3}"
    i_before_e_pattern = "i.*e"
    a_a_pattern = "^a.*a$"
    end_with_vowel_pattern = "[aeiou]$"
    weird_pattern = "[ x']"
    non_start_pattern = "^[^abcdelmnops]"
    f = open("vowel_vowel_vowel.txt", 'w')
    for capital in capitals:
        if re.search(vowel_pattern, capital, re.IGNORECASE):
            f.write(f'{capital.lower()}\n')
    f.close()

    f = open("cons_cons_cons.txt", 'w')
    for capital in capitals:
        if re.search(cons_pattern, capital, re.IGNORECASE):
            f.write(f'{capital.lower()}\n')
    f.close()

    f = open("i_before_e.txt", 'w')
    for capital in capitals:
        if re.search(i_before_e_pattern, capital, re.IGNORECASE):
            f.write(f'{capital.lower()}\n')
    f.close()

    f = open("a_a.txt", 'w')
    for capital in capitals:
        if re.search(a_a_pattern, capital, re.IGNORECASE):
            f.write(f'{capital.lower()}\n')
    f.close()

    f = open("end_with_vowel.txt", 'w')
    for capital in capitals:
        if re.search(end_with_vowel_pattern, capital, re.IGNORECASE):
            f.write(f'{capital.lower()}\n')
    f.close()

    f = open("weird.txt", 'w')
    for capital in capitals:
        if re.search(weird_pattern, capital, re.IGNORECASE):
            f.write(f'{capital.lower()}\n')
    f.close()

    f = open("not_start.txt", 'w')
    for capital in capitals:
        if re.search(non_start_pattern, capital, re.IGNORECASE):
            f.write(f'{capital.lower()}\n')
    f.close()


def main():
    print("I should not be called")


if __name__ == '__main__':
    main()
