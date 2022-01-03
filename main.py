import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_file = pandas.read_csv("50_states.csv")
state_list = answer_file["state"].tolist()


game_completed = False
states_correct = []
PROMPT = "What's another state name?"
t = turtle.Turtle()
t.penup()
while not game_completed:
    answer_state = screen.textinput(title=f"{len(states_correct)}/50 States Correct", prompt=PROMPT).title()
    if len(states_correct) == 50:
        print("You finished the game")
        game_completed = True
    elif (answer_state in state_list) and not (answer_state in states_correct):
        states_correct.append(answer_state)
        x_cor = int(answer_file[answer_file.state == answer_state].x)
        y_cor = int(answer_file[answer_file.state == answer_state].y)
        t.goto(x_cor, y_cor)
        t.write(answer_state, align='center', font=('Arial', 8, 'normal'))


screen.exitonclick()
