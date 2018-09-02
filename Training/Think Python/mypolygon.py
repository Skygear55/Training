import turtle
import math
bob = turtle.Turtle()


def square(t , length): # t is a turtle , length is the length of a side 
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
def polygon(t , length , n): # t is a turtle , length is the length of a side n is number of sides of a polygon , i guess :)
    for i in range(n):
        t.fd(length)
        t.lt(n)


def circle(t , r):#t is a turtle , and r is supposed to be radius , gonna use polygon to make a circle
   circumference = 2 * math.pi * r
   n = 50
   length = circumference / n
   polygon(bob , length , n)
   
def arc(t , r , angle):#t is a turtle , and r is supposed to be radius , gonna use polygon to make a circle, angle is , well ANGLE :)
   arc_length = 2 * math.pi * r  * angle / 360
   n = int(arc_length / 3) + 1
   step_length = arc_length / n 
   step_angle = angle / n
   
   for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    
def draw_a():
    bob.fd(100)
    bob.lt(200)
    bob.fd(100)
draw_a()      
turtle.mainloop()

