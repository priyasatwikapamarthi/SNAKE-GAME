
import random
from turtle import Turtle

COLOURS = ["cyan","light sea green","dark green","lawn green","yellow green","olive","deep pink","hot pink",
           "dark magenta","royal blue","light steel blue","slate gray"]
class Food(Turtle) :
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # self.shapesize(0.5,0.5)
        colour = random.choice(COLOURS)
        self.color(colour)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        colour = random.choice(COLOURS)
        self.color(colour)
        xcor = random.randint(-280,280)
        ycor = random.randint(-280,280)
        self.goto(xcor,ycor)

