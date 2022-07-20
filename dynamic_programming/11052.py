import sys

N = int(sys.stdin.readline())

P = list(map(int, sys.stdin.readline().split()))

dp = list([0] * (N + 1))

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + P[j-1])

print(dp[len(dp)-1])