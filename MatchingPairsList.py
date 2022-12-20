#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pair = 0
    for i in range(n):
        if ar[i] != 0:
            for j in range(i+1,n):
                if ar[i] == ar[j]:
                    ar[i]= 0
                    ar[j] = 0
                    pair += 1
                    break
    return pair
            
        

            
            
        
print(sockMerchant(5,[1,2,1,2,5]))