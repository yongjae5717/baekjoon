import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
if B + C > 59:
    A += (B + C) // 60
    B = B + C - 60 * ((B + C) // 60)
else:
    B = B + C
if A > 23:
    A = A - 24

print(A, B)