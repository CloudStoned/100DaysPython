import turtle as t
import random

tur = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r,g,b)
    return random_col

tur.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tur.color(random_color())
        tur.circle(100)
        tur.setheading(tur.heading() + size_of_gap)

draw_spirograph(1)

screen = t.Screen()
screen.exitonclick()