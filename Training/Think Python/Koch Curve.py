import turtle 

karcho = turtle.Turtle()

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
    
def snowflake(t, n):
    for i in range(4):    
         koch(t, n)
         t.rt(120)
    
    
snowflake(karcho, 100, )
turtle.mainloop()