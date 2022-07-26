import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

cars = CarManager()

player1 = Player()
scoreboard = Scoreboard()

screen.onkey(fun=player1.up, key="Up")
screen.onkey(fun=player1.turn_left, key="Left")
screen.onkey(fun=player1.turn_right, key="Right")
screen.onkey(fun=player1.down, key="Down")

cars.create_cones()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()
    if player1.ycor() > 280:
        player1.respawn()
        scoreboard.score_point()
        cars.speed_up()
        cars.update_cones()

    for car in cars.all_cars:
        if car.distance(player1) < 20:
            scoreboard.lost()
            game_is_on = False
    for cones in cars.all_cones:
        if cones.distance(player1) < 20:
            scoreboard.lost()
            game_is_on = False

screen.exitonclick()
