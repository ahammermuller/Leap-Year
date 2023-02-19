from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = list()

x = -230
y = 100
for data in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    y = y -30
    new_turtle.goto(x ,(y))
    new_turtle.color(colors[data])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

screen.title("Welcome to the turtle race!")

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You have won! The {winning_color} turtle is the winner!')
            else:
                print(f'You have lost! The {winning_color} turtle is the winner!')
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    
  
        print(turtle)

screen.exitonclick()