# pylint: disable=print-statement
import random

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
        if A[i] == A[j]:
            break
        swap(A, i, j)

def quicksort(A, l, r):
    if l < r:
        pivot(A, A[l], l, r)
        quicksort(A, l, r - 1)
        quicksort(A, l + 1, r)

newList = [random.randint(-100, 100) for i in range(20)]
print("List:", newList)
quicksort(newList, 0, len(newList) - 1)
print('Sorted List: ', newList)