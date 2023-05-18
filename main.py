import turtle
from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def forwardKey():
    t.forward(10)

def backwardKey():
    t.backward(10)

def rightTurn():
    t.right(10)

def leftTurn():
    t.left(10)

s.onkeypress(forwardKey, "w")
s.onkeypress(backwardKey, "s")
s.onkeypress(rightTurn, "d")
s.onkeypress(leftTurn, "a")
s.listen()

s.exitonclick()
