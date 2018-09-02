
    
def gcdIter(a, b):
  d = b
  while (a%d != 0 or b%d != 0):
      d = a
  return d
 




print(gcdIter(6, 12))