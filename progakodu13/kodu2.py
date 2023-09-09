from turtle import *

penup()
setpos(-300,-300) #geeksforgeeks
pendown()
def kujund(p):
    if p >= 1:
        forward(p*2)
        backward(p)
        left(90)
        forward(p*2)
        backward(p)
        right(90)
        kujund(p/(2**(1/2)))
print(screensize())
kujund(100)