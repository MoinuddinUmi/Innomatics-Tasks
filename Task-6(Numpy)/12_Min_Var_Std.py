# Task6_Q12
# You are given a 2-D array of size NXM.
# Your task is to find:
# The mean along axis 1
# The var along axis 0
# The std along axis 

# Input Format :
# The first line contains the space separated values of N and M.
# The next N lines contains M space separated integers.

import numpy
n,m=map(int,input().split())

a=numpy.array([list(map(int,input().split())) for i in range(n)])
print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
print(round(numpy.std(a,None),11))