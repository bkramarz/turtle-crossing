import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

FINISH_LINE_Y = 280

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    create_cars = randint(1, 10)
    if create_cars > 8:
        new_car = CarManager()
        cars.append(new_car)
    for car in cars:
        car.car_move(scoreboard.level)
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > FINISH_LINE_Y:
        player.reset_player()
        level = scoreboard.level_up()

screen.exitonclick()
