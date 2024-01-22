import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing the street")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# turtle movement
screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)  # page will refresh every 0.1 sec0
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    scoreboard.update_scoreboard()



    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    # detect  when turtle get the edge of the window, restart the ame
    if player.is_at_finish_line():
        player.reset()
        car_manager.speed_up()
        scoreboard.increase_level()





screen.exitonclick()