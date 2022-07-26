import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
NUM_OF_CONES = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cones = NUM_OF_CONES
        self.all_cones = []

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_cones(self):
        for num in range(self.cones):
            num = Turtle()
            num.penup()
            num.shape("triangle")
            num.left(90)
            num.color(random.choice(COLORS))
            cone_y = random.randint(-250, 250)
            cone_x = random.randint(-250, 250)
            num.goto(cone_x, cone_y)
            self.all_cones.append(num)

    def update_cones(self):
        self.cones += 1
        self.create_cones()

