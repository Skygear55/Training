#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.

def diagonalDifference(arr):
    left = []
    right = []
    count = 0
    fN = n
    while count < n:
        left.append(arr[count][count])
        right.append(arr[count][fN - 1])      
        count +=1
        fN -= 1
    
    sumL = abs(sum(left))    
    sumR = abs(sum(right))
    return abs(sumL - sumR)

print(diagonalDifference(59))

if __name__ == '__main__':                 
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
                 
    fptr.write(str(result) + '\n')

    fptr.close()
