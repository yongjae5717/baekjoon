import sys

"""
Rule
계단은 한번에 한개 또는 두개 오를 수 있다.
연속 3개의 계단을 모두 밟아서는 안된다
마지막 도착 계단은 반드시 밟아야 한다
"""

N = int(sys.stdin.readline())

stairs = [0] + [int(sys.stdin.readline()) for _ in range(N)]

dp = [0] * (N + 1)
dp[1] = stairs[1]
for i in range(1, N+1):
    if i == 2:
        dp[2] = stairs[1] + stairs[2]
    elif i == 3:
        dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    else:
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[N])