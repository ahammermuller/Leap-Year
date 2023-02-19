from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def counter_clockwise():
    tim.right(-20)

def clockwise():
    tim.left(20)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()


