import sys

N = int(sys.stdin.readline())
houses = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

d = list([0] * 3 for _ in range(N))
d[0] = houses[0]

for i in range(1, N):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + houses[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + houses[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + houses[i][2]

result = min(d[N-1])
print(result)