

def display_all(this_dict):
    """
    Function to print the keys and values stored in a given dictionary.
    :param this_dict:
    """
    for province, capital in this_dict.items():
        print(f'{capital} is the capital city of {province}')


def get_capital_city(province_name, this_dict):
    """
    Function to print a capital city of a given province from a dictionary or print that the name was not found.
    :param province_name:
    :param this_dict:
    """
    print(this_dict.get(province_name, "province name was not found"))


def add_element(province_name, capital_city, this_dict):
    """
    Function to add a given key-value to a dictionary.
    :param province_name:
    :param capital_city:
    :param this_dict:
    """
    this_dict[province_name] = capital_city
    print(this_dict)


def remove_item(province_name, this_dict):
    """
    Function to remove a given key from a dictionary
    :param province_name:
    :param this_dict:
    """
    if province_name in this_dict:
        del this_dict[province_name]
        print(this_dict)
    else:
        print("province name was not found")


def get_total_population(this_dict):
    """
    Function to sum the total population of each province in a given dictionary.
    :param this_dict:
    :return: total population
    """
    total_population = 0
    for province in this_dict:
        total_population += this_dict[province]["population"]
    return total_population


def get_another_capital_city(province_name, this_dict):
    """
    Function to get the name of the capital of the given province.
    :param province_name:
    :param this_dict:
    :return: capital or None if the name of the province doesn't exist
    """
    if province_name in this_dict:
        capital = this_dict[province_name]["capital"]
        return capital
    else:
        return "None"


def get_largest_city(province_name, this_dict):
    """
    Function to get the name of the largest city of the given province.
    :param province_name:
    :param this_dict:
    :return: largest city or None if the name of province doesn't exist.
    """
    if province_name in this_dict:
        largest = this_dict[province_name]["largest"]
        return largest
    else:
        return "None"


def get_smallest_province(this_dict):
    """
    Function to return the province with the smallest population of a given dictionary.
    :param this_dict:
    :return: name of the province
    """
    population_list = []
    for province in this_dict:
        population = this_dict[province]["population"]
        population_list.append(int(population))
        population_list.sort()
    for province in this_dict:
        if population_list[0] == this_dict[province]["population"]:
            return province.title()


def get_largest_province(this_dict):
    """
    Function to return the province with the largest population of a given dictionary.
    :param this_dict:
    :return: name of the province
    """
    population_list = []
    for province in this_dict:
        population = this_dict[province]["population"]
        population_list.append(int(population))
        population_list.sort()
    for province in this_dict:
        if population_list[-1] == this_dict[province]["population"]:
            return province.title()


def get_province_description(province_name, this_dict):
    """
    Function to display a description (province name, population, capital and largest city) for the given province
    name.
    :param province_name:
    :param this_dict:
    """
    if province_name in this_dict.keys():
        capital = this_dict[province_name]["capital"]
        largest = this_dict[province_name]["largest"]
        population = this_dict[province_name]["population"]
        if capital == largest:
            return f"{province_name.title()} has a population of {population}, " \
                   f"whose capital and largest city is {largest.title()}."
        else:
            return f"{province_name.title()} has a population of {population}, " \
                   f"whose capital is {capital.title()} and largest city is {largest.title()}."
