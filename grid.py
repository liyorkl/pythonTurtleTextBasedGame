from turtle import *
g = Turtle()  # make turtle for grid

screen = Screen()

grid_list = [
    "a1", "a2", "a3", "a4",
    "b1", "b2", "b3", "b4",
    "c1", "c2", "c3", "c4",
    "d1", "d2", "d3", "d4"
]
gridx = {'1': -300, '2': -150, '3': 0, '4': 150}
gridy = {'a': 150, 'b': 0, 'c': -150, 'd': -300}


n = Turtle()  # making a new profile for a seperate set of turtle code
n.hideturtle()
n.speed(0)
n.pensize(0)


def gridno():  # defining the code so that the turtle draws the grid numbers respectively
    for t in grid_list:
        n.pu()
        n.setpos((gridx[t[1]]+10, gridy[t[0]]+125))
        t = t.upper()
        n.write(t, font=("Times", 12, "normal"))


def grid(length):  # draws playing grid
    screen.tracer(0)
    g.hideturtle()
    g.speed(0)
    g.pensize(0)
    g.penup()
    g.setpos(-length/2, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/2, -length/4)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/2, 0)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/2, length/4)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/2, length/2)
    g.pendown()
    g.fd(length)
    g.penup()

    g.seth(90)

    g.setpos(-length/2, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(-length/4, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(0, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(length/4, -length/2)
    g.pendown()
    g.fd(length)
    g.penup()
    g.setpos(length/2, -length/2)
    g.pendown()
    g.fd(length)
    g.seth(0)
    g.penup()
    gridno()
    screen.tracer(1)
