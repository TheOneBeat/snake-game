from turtle import Turtle


class Score(Turtle):# Create a class called Score
    def __init__(self):# The main function of the class
        super().__init__()# Call the init function of the parent class
        self.score = 0# The score of the player
        self.color("white")# Set the color of the turtle
        self.penup()# Don't draw when the turtle moves
        self.goto(0, 225)# Set the position of the turtle
        self.hideturtle()# Hide the turtle
        self.updateScore()# #we call the main function of the class

    def updateScore(self):# The main function of the class
        self.write(f"Score : {self.score}", True, align="center", font=('serif', 12, 'normal'))
        # Write the score on the screen

    def increaseScore(self):# Increase the score by 1
        self.score += 1

    def refresh(self):# Refresh the score
        self.clear()# Clear the screen
        self.penup()# Don't draw when the turtle moves
        self.goto(0, 225)# Set the position of the turtle
        self.updateScore()# Update the score
