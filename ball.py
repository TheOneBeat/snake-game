from turtle import Turtle
from random import randint


class Ball(Turtle):# Create a class called Ball
    def __init__(self):# The main function of the class
        super().__init__()#we make the ball a child of the turtle class,
        # making it inherit all the methods and attributes of the turtle class
        self.shape("circle")# Set the shape of the turtle
        self.penup()# Don't draw when the turtle moves
        self.appear()#we call the main function of the class
        self.color("blue")# Set the color of the turtle
        self.resizemode("user")# Set the resize mode to user
        self.shapesize(0.5, 0.5, 1)#we make the ball appear in a random position on the screen

    def appear(self):# The main function of the class
        self.goto((randint(-220, 220), randint(-220, 220)))#we make the ball appear in a random position on the screen


