from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


color = [ "green","red","blue","purple","orange","pink","black","yellow","grey","brown"]

class Car_manager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):  
        random_chance = random.randint(1,6)
        if random_chance == 1 :
            new_car = Turtle("square")
            new_car.color(random.choice(color))
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.goto(300,random.randint(-280,280))
            self.all_car.append(new_car)

    def move_cars(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def level_up(self):        
        self.car_speed += MOVE_INCREMENT
    
