import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = lst[0]
for i in range(1, N):
    dp[i] = max(dp[i-1] + lst[i], lst[i])
print(max(dp))