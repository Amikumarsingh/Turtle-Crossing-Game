from turtle import Turtle, Screen
from player import Player
from car_manager import Car_manager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("white")
screen.setup(width=800,height=600)

car_manager = Car_manager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_upward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
  
    '''Detect collision with the car'''
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    '''Detect sucessfull crossing'''
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()     
    


screen.exitonclick()