

from turtle import Turtle
POSITIONS = [(0,0),(-20,0),(-40,0)]
DISTANCE = 20
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
    def create_snake(self):
        for key in POSITIONS:
            self.add_segment(key)

    def add_segment(self,position) :
        tim = Turtle("circle")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.turtles.append(tim)

    def extend(self):
        self.add_segment(self.turtles[-1].position())
    def move_forward(self):
        for key in range(len(self.turtles) - 1, 0, -1):
            position = self.turtles[key - 1].pos()
            self.turtles[key].goto(position)
        self.turtles[0].fd(DISTANCE)

    def up(self):
        if self.turtles[0].heading() != 270 :
            self.turtles[0].setheading(90)
    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)
    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)
    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)


