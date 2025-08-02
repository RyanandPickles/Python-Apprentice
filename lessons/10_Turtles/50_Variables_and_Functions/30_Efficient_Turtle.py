
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):

    angle = 360/sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(100)                              # Move tina forward by the forward distance
        tina.left(angle)                              # Turn tina left by the left turn


draw_polygon(4)                        # Draw a square

tina.goto(100,100)
draw_polygon(5)                        # Draw a pentagon

tina.goto(200,200)                                   # Move tina to another spot on the screen

draw_polygon(6)                        # Draw a hexagon


turtle.exitonclick()                     # Close the window when we click on it
