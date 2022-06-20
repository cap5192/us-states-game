import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
score = 0
game_over = False
guessed_state = []
screen.addshape(image)
turtle.shape(image)

while game_over is False:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt = "What's another state's name? ").title()

    data = pandas.read_csv("50_states.csv")
    if answer_state == "Exit":
        break

    for i in data["state"]:
        if answer_state == i and answer_state not in guessed_state:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            current_state = data[data["state"] == answer_state]
            x_cord = int(current_state["x"])
            y_cord = int(current_state["y"])
            t.setposition(x_cord, y_cord)
            t.pendown()
            t.write(answer_state)
            guessed_state.append(answer_state)

            score += 1
            if score == 50:
                game_over = True

#states_to_learn.csv
remaining_states = []
dict = {}
for i in data["state"]:
    if i in guessed_state:
        continue
    else:
        remaining_states.append(i)
dict["state"] = remaining_states
df = pandas.DataFrame.from_dict(dict)
df.to_csv("States_To_Learn.csv", index = False, header=True)