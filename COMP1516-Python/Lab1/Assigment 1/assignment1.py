

import data
import string


def print_json_countries_and_capitals():
    """
    Function to print a tuple of lists as a json format.
    """
    json_string = ""
    print("[")
    for country, capital in data.countries_and_capitals:
        json_format = f'{{\n\t"country_name" : "{country}",\n\t"capital_name" : "{capital}"\n}}'
        result = json_string + json_format
        print(result)
    print("]")


def get_list_of_countries_whose_nth_letter_is(n, letter):
    """
    Function to search in countries if letter position is equal to the letter and append the result in a list.
    :param n:
    :param letter:
    :return: a list of countries whose nth letter matches the letter in the parameter.
    """
    countries_whose_nth_letter_is_list = []
    for county in data.countries:
        if county[n-1].lower() == letter.lower():
            countries_whose_nth_letter_is_list.append(county)
    return countries_whose_nth_letter_is_list


def get_funny_case_capital_cities(letter):
    """
    Function to retrieve all capitals with a given letter, append it to list and uppercase the letter that precedes
    and follow the given parameter.

    :param letter:
    :return: a list with funny case capital cities.
    """
    funny_case_capital_cities_list = []
    for capital in data.capitals:
        capital = capital.lower()
        if letter in capital:
            capital = list(capital)
            for index, character in enumerate(capital):
                if character == letter and index - 1 >= 0 and capital[index - 1] != letter:
                    capital[index - 1] = capital[index - 1].upper()
                if character == letter and index + 1 < len(capital) and capital[index + 1] != letter:
                    capital[index + 1] = capital[index + 1].upper()
            funny_case_capital_cities_list.append("".join(capital))
    return funny_case_capital_cities_list


def get_doubled_letter_countries():
    """
    Function to append countries with doubled letter into a list and sort the list by the doubled letter.
    :return: a list of countries sorted by the doubled letter.
    """
    double_letter_countries = []
    sorted_double_letter_countries = []
    alphabet = string.ascii_lowercase
    for country in data.countries:
        country = country.lower()
        for index, letter in enumerate(country):
            if index - 1 >= 0 and letter == country[index - 1]:
                double_letter_countries.append(country)
    for item in alphabet:
        for country in double_letter_countries:
            for index, letter in enumerate(country):
                if index - 1 >= 0 and letter == country[index - 1] and letter == item:
                    sorted_double_letter_countries.append(country)
    return sorted_double_letter_countries


def main():
    print("I should not be called")


if __name__ == '__main__':
    main()