def genPrime():
    number = 2
    numList = []
    while True: 
        test = []
        for n in numList:
            if (number % n) !=  0:
                test.append(n)
        if test == numList:
            numList.append(number)
            yield number
        number += 1