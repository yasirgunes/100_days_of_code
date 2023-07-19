import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_states = []

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

game_is_on = True
while game_is_on:

    guess = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="What's another state's name?")
    if guess.title() in states and guess.title() not in correct_states:  # if the user guessed correctly
        if len(correct_states) == 50:
            break
        correct_states.append(guess)
        coordinate_x = int(data[data["state"] == guess.title()].x.iloc[0])
        coordinate_y = int(data[data["state"] == guess.title()].y.iloc[0])
        new_state = State(coordinate_x, coordinate_y, guess.title())
    elif guess == "exit" or guess == "Exit":
        game_is_on = False

    # save the missing states into the missing_states.csv
    # missing_states = []
    # for the_state in data["state"]:
    #     if the_state not in correct_states:
    #         missing_states.append(the_state)
    missing_states = [the_state for the_state in data["state"] if the_state not in correct_states]
    missing_dict = {
        "state": missing_states
    }
    missing_states_dataFrame = pandas.DataFrame(missing_dict)
    missing_states_dataFrame.to_csv("missing_states.csv")
