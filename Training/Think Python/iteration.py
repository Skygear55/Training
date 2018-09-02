import math
def print_n(s, n):
     while n > 0:
        print(s)
        n = n - 1 



def mysqrt(a):
    while True:
        epsilon =  0.0000000000001
        x = a /2.4     
        
        y = (x + a/x) / 2         
       
        if abs(y-x) < epsilon:
                  break
        sqrt = y      
        return sqrt
        x = y
        
           
 

def test_square_root(a):
   
    print (a, end='   ') 
    print('a')
    print (mysqrt(a), end='     ')
    print('mysqrt(a)')
    print (math.sqrt(a), end='     ')
    print ('math.sqrt(a)')
    print (abs(mysqrt(a)-(math.sqrt(a))))
    print('diff')
    
test_square_root(9)
    
    
             