import sys

N = int(sys.stdin.readline())

triangle = list(list(map(int, sys.stdin.readline().split())) for i in range(N))

for i in range(2, N + 1):
    for j in range(len(triangle[-i])):
        triangle[-i][j] += max(triangle[-i+1][j], triangle[-i+1][j+1])

print(triangle[0][0])