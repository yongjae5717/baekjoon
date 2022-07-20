import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

dp = [0] * len(seq)
for i in range(len(seq)):
    dp[i] = seq[i]

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + seq[i])

print(max(dp))