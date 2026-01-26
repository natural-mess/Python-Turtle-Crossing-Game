from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANES = list(range(-240, 280, 40))
MIN_CARS_DISTANCE = 150
COOLDOWN_SPAWN = 0.5

class CarManager():

    def __init__(self):
        self.car_active = []
        self.car_recycled = []

        # Cooldown time, time gap 
        self.cooldown = COOLDOWN_SPAWN
        self.last_spawn = time.time()

        # Min distance between 2 cars
        self.min_cars_distance = MIN_CARS_DISTANCE
        # self.car_active.append(self._car_create())
        print(LANES)

    def _car_create(self, y_pos):
        """Create car"""
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.penup()
        car.setheading(180)
        car.goto((300, y_pos))
        return car
    
    def _cooldown_time(self):
        now = time.time()
        if now - self.last_spawn < self.cooldown:
            return False
        else:
            self.last_spawn = now
            return True

    def _car_distance(self, y_pos):
        for car in self.car_active:
            if car.ycor() == y_pos and (300 - car.xcor()) < self.min_cars_distance:
                return False
        return True

    def car_spawn(self):
        if not self._cooldown_time():
            return
        
        y_pos = random.choice(LANES)
        if not self._car_distance(y_pos):
            return

        if not self.car_recycled:
            self.car_active.append(self._car_create(y_pos))
        else:
            car = self.car_recycled.pop()
            car.goto(340, y_pos)
            car.showturtle()
            self.car_active.append(car)

    def car_move_reuse(self):
        """Move car forward"""
        car_active_copy = []
        for car in self.car_active:
            car.forward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -340:
                self.car_recycled.append(car)
                car.hideturtle()
                car.goto(1000, 1000)
            else:
                car_active_copy.append(car)
        self.car_active = car_active_copy

    def car_player_collision_check(self, player):
        for car in self.car_active:
            print(car.distance(player))
            if car.distance(player) <= 40:
                print("boom")
                return True
            else:
                return False