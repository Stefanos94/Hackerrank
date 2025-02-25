#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(min(n,m)//2):
        temp_list = []
        for j in range(i, n-1-i):
            temp_list.append(matrix[j][i])
        for j in range(i, m-1-i):
            temp_list.append(matrix[n-i-1][j])
        for j in range(i, n-1-i):
            temp_list.append(matrix[n-j-1][m-i-1])
        for j in range(i, m-1-i):
            temp_list.append(matrix[i][m-j-1])
        temp_list = temp_list[-r%len(temp_list):] + temp_list[:-r%len(temp_list)]
        ind = 0
        for j in range(i, n-1-i):
            matrix[j][i] = temp_list[ind]
            ind += 1
        for j in range(i, m-1-i):
            matrix[n-i-1][j] = temp_list[ind]
            ind += 1
        for j in range(i, n-1-i):
            matrix[n-j-1][m-i-1] = temp_list[ind]
            ind += 1
        for j in range(i, m-1-i):
            matrix[i][m-j-1] = temp_list[ind]
            ind += 1
    for i in range(n):
        for j in range(m):
            print(matrix[i][j],end=' ')
        print()
        

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
