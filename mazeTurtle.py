from turtle import *

penup()
forward(20)
pendown()
for i in range(20):
    forward(20*i)
    left(90)

gordon = Pen()
gordon.shape("turtle")
gordon.color("blue")
gordon.width(2)

done()