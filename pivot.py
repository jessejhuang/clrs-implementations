# pylint: disable=print-statement
import random

newList = [random.randint(-100, 100) for i in range(20)]
p = newList[0]
print("Pivot:", p)
print("List:", newList)


def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def pivot(A, p, l, r):
    i = l
    j = r
    while i < j:
        while A[i] < p:
            i += 1
        while A[j] > p:
            j -= 1
        swap(A, i, j)


pivot(newList, p, 0, len(newList) - 1)
print "Pivoted list:", newList
