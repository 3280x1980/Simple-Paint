from turtle import *

t = Turtle()
t.color('red')
t.shape('circle')
t.down()
t.speed(0)
t.pensize(5)

def draw(x,y):
    t.goto(x,y)

def move(x,y):
    t.up()
    t.goto(x,y)
    t.down()

def setblue():
    t.color("blue")

def setred():
    t.color("red")
    
def setgreen():
    t.color("green")

def setyellow():
    t.color("yellow")

def setwhite():
    t.color("white","black")

def beginf():
    t.begin_fill()

def endf():
    t.end_fill()

def clears():
    t.clear()

def up_forward():
    t.setheading(90)
    t.forward(10)

def left_forward():
    t.setheading(180)
    t.forward(10)
    
def RIGHT_forward():
    t.setheading(0)
    t.forward(10)

def down_forward():
    t.setheading(270)
    t.forward(10)

src = t.getscreen()
src.onscreenclick(move)

src.listen()
src.onkey(setred,'1')
src.onkey(setblue,'2')
src.onkey(setgreen,'3')
src.onkey(setyellow,'4')
src.onkey(setwhite,'Q')
src.onkey(beginf,'H')
src.onkey(endf,'J')
src.onkey(up_forward,'UP')
src.onkey(left_forward,'LEFT')
src.onkey(RIGHT_forward,'RIGHT')
src.onkey(down_forward,'DOWN')
src.onkey(clears,'C')


t.ondrag(draw)

