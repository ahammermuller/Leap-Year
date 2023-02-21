import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "C:\\Users\\aline\\Documents\\UDEMY\\us-states-game-start\\us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_coor)

data = pandas.read_csv("C:\\Users\\aline\\Documents\\UDEMY\\us-states-game-start\\us-states-game-start\\50_states.csv")
all_states = data.state.to_list()
guesses_states = list()


while len(guesses_states) < len(all_states):
    answer_state = screen.textinput(title=f'{len(guesses_states)} / {len(all_states)}', prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        migging_states = [state for state in all_states if state not in guesses_states]
        new_data = pandas.DataFrame(migging_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guesses_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




screen.exitonclick()