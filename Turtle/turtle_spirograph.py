import turtle
from turtle import Turtle, Screen
import random


def random_color():
    """
    Function to generate random rgb colors.
    :return: a rgb color
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap_size, tim):
    """
    Function to draw the spirograph with an informed gap size.
    :param gap_size:
    :param tim:
    :return: none
    """
    for i in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(gap_size)
        tim.color(random_color())
        tim.speed(2000)


def main():
    tim = Turtle()
    turtle.colormode(255)
    draw_spirograph(5, tim)
    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()