import turtle
import methods as meth


def draw(dis, sides, colo):
    x = turtle.Turtle()
    x.color(colo)
    ang = meth.ang(sides)
    for i in range(sides):
        x.forward(dis)
        x.left(ang)
