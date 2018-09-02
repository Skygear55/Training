def check_fermat(a, b, c, n):
    ''' checks if fermat's theorem  was right'''
    
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No , that doesn't work.")
        
def automated_check_fermat():
    prompt = input("How much is A ?\n")
    a = int(input(prompt))
    
    prompt = input("How much is B ?\n")
    b = int(input(prompt))
 
    prompt = input("How much is C ?\n")
    c = int(input(prompt))
  
    prompt = input("How much is N ?\n")
    n = int(input(prompt))
    
    check_fermat(a, b, c, n)
#you have to input the letter first , then the integer    

def is_triangle(a, b, c):
    ''' Checks if forming a triangle is possible
    c should always be the big side if there is one '''
    
    if a + b >= c:
       print("Yes")
    else:
        print("No")

def automated_is_triangle():
    prompt = input("How much is A ?\n")
    a = input(prompt)
    
    prompt = input("How much is B ?\n")
    b = input(prompt)
 
    prompt = input("How much is C ?\n")
    c = input(prompt)
    
    is_triangle(a, b, c)
    
     