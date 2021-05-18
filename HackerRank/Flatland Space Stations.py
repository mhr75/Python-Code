#!/bin/python

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    distanceMax = 0
    c=sorted(c)
    for i in range(n):
        max = n
        check = True
        for j in c:
            if i == j:
                check = False
                break
            else:
                if abs(i - j) < max :
                    max = abs(i - j)
        if(check and distanceMax < max):
                distanceMax = max
    return distanceMax

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = map(int, raw_input().rstrip().split())

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
