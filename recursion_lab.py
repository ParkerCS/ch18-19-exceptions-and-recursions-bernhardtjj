"""
Using the turtle library, create a fractal pattern.
You may use heading/forward/backward or goto and fill commands to draw
your fractal.  Ideas for your fractal pattern might include
examples from the chapter.  You can find many fractal examples online,
but please make your fractal unique.  Experiment with the variables
to change the appearance and behavior.

Give your fractal a depth of at least 5.  Ensure the fractal is contained on the screen (at whatever size you set it).
Have fun.
(35pts)
"""

import turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "cyan", "black"]

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_screen = turtle.Screen()
my_screen.bgcolor('white')
# Draw Here
my_turtle.color("black")


def draw(x, y, heading, dist, depth):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.fillcolor(colors[depth % len(colors)])
    my_turtle.down()
    my_turtle.begin_fill()
    for i in range(4):
        my_turtle.setheading(heading - 90 * i)
        my_turtle.forward(dist)
    my_turtle.end_fill()
    new_dist = dist / 1.618033  # phi
    my_turtle.backward(dist - new_dist)
    new_y = my_turtle.ycor()
    new_x = my_turtle.xcor()
    if depth > 0:
        draw(new_x, new_y, heading - 90, new_dist, depth - 1)


draw(100, -250, 180, 500, 10)
my_screen.exitonclick()

#   ____
#  / ___|__ _ _ __    _   _  ___  _   _    __ _ _   _  ___  ___ ___
# | |   / _` | '_ \  | | | |/ _ \| | | |  / _` | | | |/ _ \/ __/ __|
# | |__| (_| | | | | | |_| | (_) | |_| | | (_| | |_| |  __/\__ \__ \
#  \____\__,_|_| |_|  \__, |\___/ \__,_|  \__, |\__,_|\___||___/___/
#                     |___/               |___/
#           _           _     _   _     _       _       ___
# __      _| |__   __ _| |_  | |_| |__ (_)___  (_)___  |__ \
# \ \ /\ / / '_ \ / _` | __| | __| '_ \| / __| | / __|   / /
#  \ V  V /| | | | (_| | |_  | |_| | | | \__ \ | \__ \  |_|
#   \_/\_/ |_| |_|\__,_|\__|  \__|_| |_|_|___/ |_|___/  (_)
