#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #long version 
   # sumL = []
   # for i in ar:
    #    sumL.append(i)
  #  return sum(sumL)
  
  
  
  #list comprehension
    #sumL = [i for i in ar]   
   #return only version
    return sum(ar)


print(simpleArraySum([1, 2, 3, 5]))
