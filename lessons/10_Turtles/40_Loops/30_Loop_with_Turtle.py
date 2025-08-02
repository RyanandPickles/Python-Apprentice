
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and paste most of it! )

"""

... # Your code here
import turtle
tina=turtle.Turtle()

tina.shape('turtle')
tina.speed(2)

for i in range (5):
    tina.forward(100)
    tina.left(72)

turtle.exitonclick