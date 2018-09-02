#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    result = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1
    return result


# testcase 
#print(compareTriplets([3, 6, 8], [4, 5, 8]))