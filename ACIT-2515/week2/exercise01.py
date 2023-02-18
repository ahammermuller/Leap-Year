import string


def str2dict(string):
    """
    Function that takes a string and convert it into a dictionary.
    :param string:
    :return:
    """
    new_dictionary = {}
    for character in string:
        if character not in new_dictionary:
            new_dictionary[character] = 1
        else:
            new_dictionary[character] += 1
    return new_dictionary


def str2dict_plus(passage):
    """
    Function to remove spacial characters from a passage.
    :param passage:
    :return:
    """
    passage = passage.lower()
    bad_char = string.punctuation + ' '
    new_passage = ""
    for x in passage:
        if x not in bad_char:
            new_passage += x
    freq_dict = str2dict(new_passage)
    return freq_dict


def histogram(passage):
    """
    Function to convert the value in a dictionary to the character '*'
    :param passage:
    :return:
    """
    char_freq = str2dict_plus(passage)
    for (key, value) in char_freq.items():
        print(key, value * '*')


def count_people(filename):
    """
    Function that opens a file and count the number os lines in it.
    :param filename:
    :return:
    """
    with open(filename, "r") as fp:
        return len(fp.readlines())


print(count_people("data01.txt"))
print(histogram("Haaaah"))
print(str2dict("Haah"))
print(str2dict_plus("dat#$04DT"))
