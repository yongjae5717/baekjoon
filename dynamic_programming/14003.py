import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

dp = [(-1000000001, -1)]
temp = [0] * N

for i in range(N):
    start = 0
    end = len(dp) - 1
    while start <= end:
        mid = (start + end) // 2
        if dp[mid][0] < seq[i]:
            start = mid + 1
        else:
            end = mid - 1

    if start >= len(dp):
        temp[i] = dp[start-1][1]
        dp.append((seq[i], i))
    else:
        dp[start] = (seq[i], i)
        temp[i] = dp[start-1][1]


# print("DP", dp)
# print("TEMP", temp)
print(len(dp)-1)

result = list()
idx = dp[len(dp)-1][1]
while idx != -1:
    result.append(seq[idx])
    idx = temp[idx]

# print(result)
for i in range(len(result)-1, -1, -1):
    print(result[i], end=" ")