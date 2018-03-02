# pylint: disable=print-statement
def BottomUpRodCut(p, n):
    r = [0 for i in range(n)]
    for j in range(n):
        q = p[0]
        for i in range(j + 1):
            q = max(q, p[i] + r[j - i - 1])
        r[j] = q
    return r[n - 1]

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
for i in range(1, 10):
    print i, BottomUpRodCut(p, i)