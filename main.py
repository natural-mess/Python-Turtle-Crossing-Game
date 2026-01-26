import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

game_is_pause = False

def pause_game():
    """Set or unset game_is_pause to pause or resume game"""
    global game_is_pause
    game_is_pause ^= 1

screen.listen()
screen.onkeypress(fun=pause_game, key="space")
screen.onkeypress(fun=player.move, key="Up")

while True:
    time.sleep(0.1)
    screen.update()

    car.car_spawn()
    car.car_move_reuse()
    if car.car_player_collision_check(player):
        break

    # If user presses space, game is pause
    while game_is_pause:
        pass

screen.exitonclick()