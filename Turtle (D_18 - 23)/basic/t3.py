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

directions = [0, 90, 180, 270]
tur.pensize(15)
tur.speed("fastest")

for _ in range(200):
    tur.color(random_color())
    tur.forward(30)
    tur.setheading(random.choice(directions))