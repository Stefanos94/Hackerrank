#!/bin/python3

import math
import os
import random
import re
import sys
import math
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def merge_sort(arr):
    n = len(arr)
    if n>2:
        half = math.floor(n/2)
        arr[:half], temp1 = merge_sort(arr[:half]) 
        arr[half:], temp2 = merge_sort(arr[half:]) 
        temp = arr.copy()
        i = 0
        
        j = half
        k = 0
        swaps = half
        counter = temp1 + temp2
        while (i<half) & (j<n):
            if temp[i]>temp[j]:
                arr[k] = temp[j]
                j = j + 1
                k = k + 1
                counter = counter + swaps
                
            else:
                arr[k] = temp[i]
                i = i + 1
                k = k + 1
                swaps = swaps - 1
        if j == n:
            for l in range(i,half):
                arr[k] = temp[l]
                k = k + 1
        else:
            for l in range(j,n):
                arr[k] = temp[l]
                k = k + 1
            
        return arr, counter
                
    elif n == 2:
        if arr[0] > arr[1]:
            
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            
            return arr, 1
        else:
            return arr, 0
    return arr, 0

def insertionSort(arr):
    arr , shifts = merge_sort(arr)
    print(arr)
    return shifts
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
