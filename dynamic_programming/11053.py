import sys

N = int(sys.stdin.readline())

lst = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)


for i in range(N+1):
    temp = 0
    for j in range(i):
        if lst[j] < lst[i] and temp < dp[j]:
            temp = dp[j]
        if j == i - 1:
            dp[i] = temp + 1
print(max(dp))