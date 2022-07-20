import sys

N = int(sys.stdin.readline())
triangle = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

triangle.sort(key=lambda x: len(x), reverse=True)

# for i in triangle:
#     print(i)

for i in range(1, N):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j + 1])

print(triangle[N-1][0])