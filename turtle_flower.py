"""
turtle_flower.py: f l o w e r :)
1/03/2022
"""

import turtle

saber = turtle.Turtle()
saber.speed(7)
saber.color("red", "yellow")

saber.begin_fill()

for i in range(26):

    saber.forward(200)
    saber.left(165)
    saber.forward(200)

saber.end_fill()

turtle.done()
