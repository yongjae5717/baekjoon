"""
N가지 종류의 동전 -> 가치의 합 K원이 되도록해야한다.
각각의 동전은 몇개라도 사용할 수 있다.
출력: 경우의 수
"""

import sys

N, K = map(int, sys.stdin.readline().split())

coins = list()
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
coins.sort()

dp = list([0] * (K+1))
dp[0] = 1

for i in range(0, N):
    i_value = coins[i]
    for j in range(i_value, K+1):
        if dp[j-coins[i]] != 0:
            dp[j] += dp[j-coins[i]]
    print(dp)

print(dp[len(dp)-1])