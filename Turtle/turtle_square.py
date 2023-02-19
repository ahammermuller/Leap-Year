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

def main():
    tim = Turtle()
    turtle.colormode(255)
    tim.width(10)
    direction = [0, 90, 180, 270]
    for i in range (100):
        tim.color(random_color())
        tim.setheading(random.choice(direction))
        tim.forward(30)
        tim.speed(10)

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()