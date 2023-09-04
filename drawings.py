import cmd
import os
import random
import textwrap
import sys
import time
from turtle import *

screen = Screen()
screen.setup(600, 600)

ZONENAME = ""

zonemap = {
    'a1': {
        ZONENAME: "City Area"
    },

    'a2': {

        ZONENAME: "Bush"
    },

    'a3': {
        ZONENAME: "Stream"
    },

    'a4': {
        ZONENAME: "City Area"
    },

    'b1': {
        ZONENAME: "Bush"
    },

    'b2': {
        ZONENAME: "Stream"
    },

    'b3': {
        ZONENAME: "Stream"
    },

    'b4': {
        ZONENAME: "City Area"
    },

    'c1': {
        ZONENAME: "Stream"
    },

    'c2': {
        ZONENAME: "Stream"
    },

    'c3': {
        ZONENAME: "Bush"
    },

    'c4': {
        ZONENAME: "City Area"
    },

    'd1': {
        ZONENAME: "City Area"
    },

    'd2': {
        ZONENAME: "Bush"
    },

    'd3': {
        ZONENAME: "Bush"
    },

    'd4': {
        ZONENAME: "Shop"
    }}


gridx = {'1': -300, '2': -150, '3': 0, '4': 150}
gridy = {'a': 150, 'b': 0, 'c': -150, 'd': -300}

grid_list = [
    "a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4", "c1", "c2", "c3", "c4",
    "d1", "d2", "d3", "d4"
]


def drawstream():
    screen.tracer(0)
    for t in grid_list:
        if zonemap[t][ZONENAME] == "Stream":
            wave(gridx[t[1]], gridy[t[0]])
    screen.tracer(1)


def drawbush():
    screen.tracer(0)
    for t in grid_list:
        if zonemap[t][ZONENAME] == "Bush":
            bush(gridx[t[1]], gridy[t[0]])
    screen.tracer(1)


def drawcity():
    screen.tracer(0)
    for t in grid_list:
        if zonemap[t][ZONENAME] == "City Area":
            city(gridx[t[1]], gridy[t[0]])
    screen.tracer(1)


def drawshop():
    screen.tracer(0)
    for t in grid_list:
        if zonemap[t][ZONENAME] == "Shop":
            shop(gridx[t[1]], gridy[t[0]])
    screen.tracer(1)

####################################


o = Turtle()  # making a new profile for a seperate set of turtle code
o.speed(0)
o.hideturtle()
o.pu()


def wave(x, y):  # defining the code for drawing the stream
    o.color('blue')
    for l in range(5):
        o.setpos(x, y + ((80 * l) / 3) + 3)
        o.pd()
        for z in range(100):
            o.fd(.43)
            o.lt(.5)
        for z in range(200):
            o.fd(.43)
            o.rt(.5)
        for z in range(100):
            o.fd(.43)
            o.lt(.5)
        o.pu()


def bush(x, y):  # defining the code for drawing the bush
    o.pu()
    o.color('green')
    # calling the smaller drawings and combining them for bush squares
    bushbush(x + 20, y + 10)
    bushbush(x + 75, y + 90)
    bushgrass(x + 110, y + 10)
    bushgrass(x + 90, y + 50)
    bushgrass(x + 30, y + 90)


def bushbush(x, y):  # defining a smaller drawing for the bush squares
    o.setpos(x, y)
    o.seth(0)
    o.color('#32FB1A')  # changing the turtle colour using hex code
    o.fillcolor('#32FB1A')
    o.begin_fill()  # fill code to colour a whole area rather than just lines
    o.pd()
    o.fd(45)
    for z in range(20):
        o.fd(2.5/2)
        o.lt(6.5)
    for z in range(9):
        o.fd(3/2)
        o.lt(8)
    o.seth(90)
    for z in range(45):
        o.fd(2.865/2)
        o.lt(4)
    o.seth(180)
    for z in range(20):
        o.fd(2.5/2)
        o.lt(6.5)
    for z in range(9):
        o.fd(3/2)
        o.lt(8)
    o.end_fill()  # fill code to colour a whole area rather than just lines
    o.pu()


def bushgrass(x, y):  # defining a smaller drawing for the bush squares
    o.setpos(x, y)
    o.seth(0)
    o.pd()
    o.seth(90)
    o.fillcolor('green')
    o.begin_fill()  # fill code to colour a whole area rather than just lines
    for z in range(10):
        o.fd(3)
        o.lt(3)
    o.pu()
    o.setpos(x, y)
    o.seth(90)
    o.pd()
    for z in range(10):
        o.fd(2.5)
        o.lt(6)
    o.pu()
    o.setpos(x, y)
    o.seth(90)
    o.pd()
    for z in range(10):
        o.fd(2)
        o.lt(9)
    o.pu()
    o.setpos(x, y)
    o.seth(90)
    o.pd()
    for z in range(10):
        o.fd(3)
        o.rt(2)
    o.pu()
    o.setpos(x, y)
    o.seth(90)
    o.pd()
    for z in range(10):
        o.fd(2)
        o.rt(8)
    o.end_fill()  # fill code to colour a whole area rather than just lines
    o.pu()


def city(x, y):  # defining the code for drawing the city area
    o.pu()
    o.seth(0)
    o.color('black')
    o.fillcolor('silver')
    o.setpos(x + 75, y + 10)
    o.pd()
    o.begin_fill()  # fill code to colour a whole area rather than just lines
    o.seth(150)
    o.fd(40)
    o.seth(90)
    o.fd(80)
    o.seth(330)
    o.fd(40)
    o.seth(30)
    o.fd(40)
    o.seth(270)
    o.fd(80)
    o.seth(210)
    o.fd(40)
    o.end_fill()  # fill code to colour a whole area rather than just lines
    o.pu()
    o.fillcolor('lightgrey')
    o.begin_fill()  # fill code to colour a whole area rather than just lines
    o.setpos(x + 40, y + 110)
    o.pd()
    o.seth(30)
    o.fd(40)
    o.seth(330)
    o.fd(40)
    o.seth(210)
    o.fd(40)
    o.seth(150)
    o.fd(40)
    o.end_fill()  # fill code to colour a whole area rather than just lines
    o.pu()
    o.setpos(x + 75, y + 10)
    o.seth(90)
    o.pd()
    o.fd(80)
    o.pu()
    leftwindow(x + 60, y + 70)
    leftwindow(x + 45, y + 77.5)
    leftwindow(x + 60, y + 50)
    leftwindow(x + 45, y + 57.5)
    rightwindow(x + 80, y + 65)
    rightwindow(x + 95, y + 72.5)
    rightwindow(x + 80, y + 45)
    rightwindow(x + 95, y + 52.5)


def leftwindow(x, y):  # defining one of the windows so it is repeatable
    o.setpos(x, y)
    o.seth(90)
    o.pd()
    o.fd(10)
    o.seth(330)
    o.fd(10)
    o.seth(270)
    o.fd(10)
    o.seth(150)
    o.fd(10)
    o.pu()


def rightwindow(x, y):  # defining one of the windows so it is repeatable
    o.setpos(x, y)
    o.seth(90)
    o.pd()
    o.fd(10)
    o.seth(30)
    o.fd(10)
    o.seth(270)
    o.fd(10)
    o.seth(210)
    o.fd(10)
    o.pu()


def shop(x, y):  # defining the code for drawing the shop
    o.color('black')
    o.fillcolor('#EEAC33')  # changing the turtle colour using hex code
    o.setpos(x + 40, y + 25)
    o.seth(90)
    o.begin_fill()  # fill code to colour a whole area rather than just lines
    o.pd()
    o.fd(45)
    o.seth(0)
    o.fd(10)
    o.seth(270)
    o.fd(30)
    o.seth(0)
    o.fd(50)
    o.seth(90)
    o.fd(30)
    o.seth(0)
    o.fd(10)
    o.seth(270)
    o.fd(45)
    o.seth(180)
    o.fd(70)
    o.end_fill()  # fill code to colour a whole area rather than just lines
    o.pu()
    o.fillcolor('#C88912')  # changing the turtle colour using hex code
    o.begin_fill()  # fill code to colour a whole area rather than just lines
    o.setpos(x + 52.5, y + 45)
    o.pd()
    o.seth(225)
    o.fd(10)
    o.seth(0)
    o.fd(60)
    o.seth(135)
    o.fd(10)
    o.seth(180)
    o.fd(45)
    o.end_fill()  # fill code to colour a whole area rather than just lines
    o.pu()
    o.setpos(x + 36, y + 100)
    o.fillcolor('#FA3333')  # changing the turtle colour using hex code
    o.begin_fill()  # fill code to colour a whole area rather than just lines
    o.seth(268.5)
    o.pd()
    o.fd(30)
    o.seth(0)
    o.fd(80)
    o.seth(91.5)
    o.fd(30)
    o.seth(180)
    o.fd(80)
    o.end_fill()  # fill code to colour a whole area rather than just lines


screen.tracer(1)


def drawmap():
    drawstream()
    drawbush()
    drawcity()
    drawshop()
