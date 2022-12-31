from turtle import Turtle


class Snake:# The snake class
    def __init__(self):
        self.l = []# The list of turtles to represent the snake
        self.length = 3# The length of the snake at the start
        self.pos = 0# The position of the first turtle in the snake
        self.createSnake()#we call the main function of the class


    def createSnake(self):# The main function of the class
        for i in range(self.length):# For each part of the snake
            tim = Turtle()# Create a new turtle
            tim.penup()# Don't draw when the turtle moves
            tim.color("white")# Set the color of the turtle
            tim.shape("square")# Set the shape of the turtle
            tim.resizemode("user")# Set the resize mode to user
            tim.shapesize(1, 1)# Set the size of the turtle
            tim.goto((self.pos, 0))# Set the position of the turtle
            self.l.append(tim)# Add the turtle to the list
            self.pos -= 20# Path: main.py

    def turnRight(self):# When the user press the right arrow, the snake will go right
        self.l[0].seth(0)


    def turnLeft(self):# When the user press the left arrow, the snake will go left
        self.l[0].seth(180)


    def goUp(self):# When the user press the up arrow, the snake will go up
        self.l[0].seth(90)


    def goDown(self):# When the user press the down arrow, the snake will go down
        self.l[0].seth(270)


    def moveSnake(self):# Move the snake
        for i in range(len(self.l)-1, 0, -1):# For each part of the snake
            new_pos = self.l[i-1].pos()# Get the position of the previous part of the snake
            self.l[i].goto(new_pos)# Set the position of the current part of the snake to the position of the previous part of the snake
        self.l[0].fd(20)#make the snake head move of 20 of distance from the previous position

    def growSnake(self):# Grow the snake
        tim = Turtle()# Create a new turtle
        tim.penup()# Don't draw when the turtle moves
        tim.shape("square")# Set the shape of the turtle
        tim.color("white")# Set the color of the turtle
        position = (self.l[-1].xcor(), self.l[-1].ycor())# Get the position of the last part of the snake
        tim.setpos(position)# Set the position of the new part of the snake
        self.l.append(tim)# Add the new part of the snake to the list
        self.length += 1# Increase the length of the snake








