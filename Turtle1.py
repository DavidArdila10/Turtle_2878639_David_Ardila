from turtle import Turtle, Screen

def draw_shape(turtle, color, sides):
    angle = -360 / sides
    turtle.pencolor(color)
    for _ in range(sides):
        turtle.fd(100)
        turtle.left(angle)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pensize(5)
timmy_the_turtle.speed(float("10"))


colors = ["violet", "red", "blue", "green", "orange", "black", "gray", "brown"]
num_shapes = len(colors)
start_sides = 3

for i in range(start_sides, start_sides + num_shapes):
    draw_shape(timmy_the_turtle, colors[i - start_sides], i)

screen = Screen()
screen.exitonclick()
