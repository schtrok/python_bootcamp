import turtle
import pandas

from state import State

# init screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# load states image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# load states from csv
states = pandas.read_csv("50_states.csv")
total_states_num = len(states.state)
guessed_states: list[turtle.Turtle] = []

while len(guessed_states) < total_states_num:
    # ask for user input
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{total_states_num} States Correct",
        prompt="What's another state's name?",
    )

    # ask again if user did not provide an input
    if not answer_state:
        continue

    # if user did provide input, check if state exists and go back to input if it doesn't
    answer_state = answer_state.title()
    result_state = states[states.state == answer_state]
    if not len(result_state):
        continue

    # if it exists, put it on the map and move it from not quessed to guessed states
    new_state = State(
        answer_state,
        float(result_state.x),
        float(result_state.y),
    )
    states = states.loc[states.state != answer_state]
    guessed_states.append(new_state)

# main loop
turtle.mainloop()
