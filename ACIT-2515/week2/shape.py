def triangle(size):
    """ This function must print a triangle using the # character on the screen.
    Example:
    >>> triangle(5)
    #
    ##
    ###
    ####
    #####

    """
    for i in range(1, size + 1):
        print('#' * i)



def rectangle(width, height):
    """ This function must print a rectangle with the correct dimensions on the screen with #.

    !!! The rectangle is not filled with # !!!

    Examples:
    >>> rectangle(0, 0)

    >>> rectangle(1, 1)
    #

    >>> rectangle(3, 1)
    ###

    >>> rectangle(10, 3)
    ##########
    #        #
    ##########

    """
    if height > 0:
        print("#" * width)

    for line_number in range(height - 2):
        print("#" + " " * (width - 2) + "#")

    if height > 1:
        print("#" * width)




triangle(0)
triangle(10)

rectangle(10, 3)
rectangle(-1, -1)