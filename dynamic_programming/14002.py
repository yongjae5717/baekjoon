import sys

N = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))


dp = [1] * N
for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

count = max(dp)
result = list()
output = ""

for k in range(N-1, -1, -1):
    # print(dp[k])
    if dp[k] == count:
        count -= 1
        result.append(seq[k])

result.reverse()
for t in result:
    output += str(t) + " "

print(max(dp))
print(output)