def recurse(n, s):
    '''
    
    If value of n = 0 s will be printed
    if not recurse will repeat , this time n
    will be with 1 less and s will be with n more.
    This will repeat until n = 0 and s will be printed
    
    '''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

  
'''
Stack Diagram Of recurse(n, s):
    _main_ --->
    
    recurse ---> n = 3
                 s = 0
    recurse ---> n = 2
                 s = 3
    recurse ---> n = 1  
                 s = 5
    recurse ---> n = 0
                 s = 6            
'''