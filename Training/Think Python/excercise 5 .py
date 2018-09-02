import turtle 
kircho = turtle.Turtle()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

draw (kircho, 10, -1)

turtle.mainloop()


def koch(t, x):
    '''
    Draws a Koch curve using 
    t = turtle 
    x = length
    '''
    if x < 10:
        t.fd(x)
        return
    m = x/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)