import math

def nearMiss(n):
    ans = 0

        for i in range(1, n + 1):
        for j in range(i, n + 1):
            x = i * i + j * j