# pylint: disable=print-statement

import copy

# Bottom up implementation of coin change
# Optimal Substructure property: Making change for value n is equivalent to 
# C plus making change for some value n - c
# Build table of optimal solution for each value
def coinChange(C, n):
    r = [[0 for __ in C] for __ in range(n + 1)]
    for i in range(1,n+1):#Compute optimal solution for value i
        q = [float('inf') for __ in C]
        for j, c in enumerate(C): #decide whether to include coin c or not
            if i >= c:
                x = copy.deepcopy(r[i - c])
                x[j] += 1
                if sum(x) < sum(q):
                    q = x         
        r[i] = q
    return r[n]

n = 55
C = [1, 5, 10, 25, 100]
print(coinChange(C, n))

# Test case for which greedy will not hold
n = 6
C = [1, 3, 4]
print(coinChange(C,n))