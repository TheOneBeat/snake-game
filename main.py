from snake import Snake
from turtle import Turtle
from ball import Ball
from score import Score
from turtle import Screen
import time

theSnake = Snake()# Create the snake
theBall = Ball()# Create the food
theScore = Score()# Create the score
myscreen = Screen()# Create the screen
myscreen.bgcolor('black')# Set the background color
myscreen.setup(width=500, height=500)# Set the size of the screen
myscreen.title("the snake's game")# Set the title of the screen

continueGame = True# This variable will be used to know if the game is over or not

myscreen.onkey(theSnake.goUp, "Up")# When the user press the up arrow, the snake will go up
myscreen.onkey(theSnake.goDown, "Down")# When the user press the down arrow, the snake will go down
myscreen.onkey(theSnake.turnRight, "Right")# When the user press the right arrow, the snake will go right
myscreen.onkey(theSnake.turnLeft, "Left")# When the user press the left arrow, the snake will go left
myscreen.listen()# Listen to the user's input
myscreen.tracer(0)# Disable the animation
while continueGame:# While the game is not over

    myscreen.update()# Update the screen
    time.sleep(0.1)# Wait 0.1 second
    theSnake.moveSnake()# Move the snake

    if theSnake.l[0].distance(theBall) < 15:# If the snake's head is close to the food
        theSnake.growSnake()# Grow the snake
        theBall.appear()# Make the food appear in a random position
        theScore.increaseScore()# Increase the score
        theScore.refresh()# Refresh the score

    if theSnake.l[0].xcor() > 230 or theSnake.l[0].ycor() > 230 or theSnake.l[0].xcor() < -230 or theSnake.l[
        0].ycor() < -230:# If the snake's head is out of the screen
        tim = Turtle()# Create a new turtle
        tim.color("red")# Set the color of the turtle to red
        tim.write("Game over", True, align="center", font=('Serif', 30, 'normal'))# Write "Game over" on the screen
        continueGame = False# The game is over

    for i in range(1, theSnake.length):# For each part of the snake
        if theSnake.l[0].distance(theSnake.l[i]) < 10:# If the snake's head is close to one of its part
            tim = Turtle()# Create a new turtle
            tim.color("red")# Set the color of the turtle to red
            tim.write("Game over", True, align="center", font=('Serif', 30, 'normal'))# Write "Game over" on the screen
            continueGame = False# The game is over

myscreen.exitonclick()# When the user click on the screen, the game will close
