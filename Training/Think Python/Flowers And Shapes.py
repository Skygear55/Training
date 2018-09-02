import turtle
import math

bob = turtle.Turtle()
def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle) 
        
def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
    
def petal(t , r, angle )   :
   ''' draws a petal using two arcs .
   t = turtle 
   r = radius of the arcs
   angle : angle(degrees tahat subtends the arcs
   '''
   for i in range(2):
       arc(bob , r , angle)
       t.lt(180-angle)
def flower(t, n , r , angle):       
    for i in range(n):
        petal (t , r , angle) 
        t.lt(100-angle)
        
        
flower(bob , 15 , 100 , 30 )
turtle.mainloop()