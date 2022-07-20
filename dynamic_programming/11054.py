import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

dp = [0] * N

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

seq.reverse()
dp2 = [0] * N
for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2.reverse()

result_dp = [0] * N
for i in range(N):
    result_dp[i] = dp[i] + dp2[i] + 1

# print(dp)
# print(dp2)
# print(result_dp)
print(max(result_dp))