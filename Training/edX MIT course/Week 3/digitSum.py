def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    i = 0
    sumL = []
    def split(N, i):
        nS = str(N)      
        if i == len(nS):
            return sum(sumL)
        else:
            sumL.append(int(nS[i]))
            return split(N, i+1)
             
    return split(N, i)
  
    



print(sumDigits(1555))