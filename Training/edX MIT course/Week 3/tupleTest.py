def multBy3(x):
    return x*3

def add5(y):
    return y+5


def applyfunc(f, g, p):
    return f(p), g(p)


print(applyfunc(multBy3, add5, 3))

def returnArgsAsList(das, *lis):
    print(lis)
    print(das)
    
    
returnArgsAsList(2, 1,2,3,5,6,'byn')