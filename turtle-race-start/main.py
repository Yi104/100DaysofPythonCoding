from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title= "make your bet", prompt ="which turtle will win the race?")
y_positions=[-150,-100,-50,50,100,150]
colors=["red","orange","yellow","green","cyan","purple"]
all_turtles=[]

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y = y_positions[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            win_color= turtle.pencolor()
            if win_color == user_bet:
                print(f"you won, the winning turtle is {win_color}")
            else:
                print(f"you lose, the winning turtle is {win_color}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
















screen.exitonclick()