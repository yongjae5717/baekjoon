"""
수열이 존재할 때, 가장 긴 감소하는 부분 수열의 길이
"""

import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))