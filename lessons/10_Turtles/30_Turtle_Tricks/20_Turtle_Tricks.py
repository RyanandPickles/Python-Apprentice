"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here
tina.forward(100)
tina.left(72)
tina.pencolor('red')
tina.forward(100)
tina.left(72)
tina.pencolor('orange')
tina.forward(100)
tina.left(72)
tina.pencolor('yellow')
tina.forward(100)
tina.left(72)
tina.pencolor('green')
tina.forward(100)
tina.left(72)
tina.pencolor('blue')
turtle.exitonclick()                    # Close the window when we click on it
