import turtle
from turtle import Turtle, Screen
import colorgram
import random


def color_generator():
    """
    Function to select 30 rgb colors from an image and save them into a list.
    :return:  a list of rgb colors.
    """
    rgb_colors = []
    colors = colorgram.extract('image.png', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)

def random_color():
    """
    Function to select random rgb colors from a list
    :return: a random rgb tuple
    """
    generated_colors_list = [(230, 226, 228), (34, 108, 167), (223, 229, 235), (227, 233, 230), (245, 77, 36),
                             (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84),
                             (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30),
                             (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), (155, 212, 203),
                             (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), (35, 55, 46), (99, 93, 2)]
    color = (random.choice(generated_colors_list))
    return color


def painting(tim):
    """
    Function to paint a square (10x10) with 100 dots.
    :param tim:
    :return: none
    """
    for x in range(0,5):
        for i in range(0,10):
            tim.dot(20, random_color())
            tim.penup()
            tim.forward(50)
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(50)
        for i in range(0,10):
            tim.dot(20, random_color())
            tim.penup()
            tim.forward(50)
        tim.right(90)
        tim.forward(50)
        tim.right(90)
        tim.forward(50)

def main():
    tim = Turtle()
    turtle.colormode(255)
    tim.hideturtle()
    tim.setheading(225)
    tim.penup()
    tim.forward(380)
    tim.setheading(0)
    painting(tim)
    screen = Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()