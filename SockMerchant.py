#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs=0
    ar.sort()
    i=0
    while i<n-1:
        if(ar[i]==ar[i+1]):
            pairs=pairs+1
            i+=2
        else:
            i+=1
   # print pairs       
    return pairs
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
