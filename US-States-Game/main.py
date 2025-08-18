import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (Type 'Exit' to quit)"
    )

    if not answer_state:
        continue

    answer_state = answer_state.strip().title()

    if answer_state == "exit":
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
    else:
        screen.title(f"'{answer_state}' is not valid or already guessed.")

missing_states = [state for state in all_states if state not in guessed_states]
pandas.DataFrame(missing_states, columns=["state"]).to_csv("states_to_learn.csv", index=False)

screen.title(f"Game Over! You got {len(guessed_states)}/50. Missing saved to states_to_learn.csv")
screen.exitonclick()
