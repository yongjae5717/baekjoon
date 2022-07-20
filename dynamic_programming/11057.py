import sys

"""
오르막 수: 자리가 오름차순인 수
ex) 2234, 3678, 11119

      0 1 2 3 4 5 6 7 8 9
1자리: 1 1 1 1 1 1 1 1 1 1 (10개)
2자리: 1 2 3 4 5 6 7 8 9 10 (55개)
3자리: 1 3 6 10 15 21 28 36 45 55 (220개)

A[n][0] = 1
A[n][m] = A[n-1][m] + A[n][m-1]
"""

N = int(sys.stdin.readline())
lst = list([1] + [0] * 9 for _ in range(N))
lst[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    for j in range(1, 10):
        lst[i][j] = lst[i-1][j] + lst[i][j-1]

print(sum(lst[N-1]) % 10007)