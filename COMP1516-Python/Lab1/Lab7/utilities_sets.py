

def get_total_items(set1):
    """
    Function to print the total number of items in a set.
    :param set1:
    """
    print(len(set1))


def display_all_items(set1):
    """
    Function to print all the elements for the given set.
    :param set1:
    """
    print(set1)


def add_item(item, set1):
    """
    Function to add a given item to the set.
    :param item:
    :param set1:
    """
    set1.add(item)
    print(set1)


def remove_item(item, set1):
    """
    Function to removes a given item to the set.
    :param item:
    :param set1:
    """
    set1.remove(item)
    print(set1)


def get_the_union_of(set1, set2):
    """
    Function to print the result of the union of two sets.
    :param set1:
    :param set2:
    """
    new_set = set1.union(set2)
    print(new_set)