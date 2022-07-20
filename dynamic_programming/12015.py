import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

dp = [0]
for i in range(N):
    start = 0
    end = len(dp) - 1

    while start <= end:
        mid = (start + end) // 2
        if dp[mid] < seq[i]:
            start = mid + 1
        else:
            end = mid - 1

    if start >= len(dp):
        dp.append(seq[i])
    else:
        dp[start] = seq[i]

print(len(dp)-1)