import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

sleep_rate = 0.1
game_is_on = True
while game_is_on:
    time.sleep(sleep_rate)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    # detect turtle collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    # player makes it to the other side
    if player.ycor() > 280:
        player.made_it()
        scoreboard.keep_level()
        sleep_rate *= 0.80

screen.exitonclick()