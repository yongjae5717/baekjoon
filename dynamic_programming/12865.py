"""
가지고 다닐 배낭에 최대한 가치 있게 싸려고 한다.
여행자가 필요한 N개의 물건 (무게 W, 가치 V, 최대 K무게를 가질 수 있다.)
출력: 여행자가 배낭에 넣을 수 있는 최대 가치의 합

"""

import sys

# N: 물품의 수, K: 여행자가 버틸 수 있는 무게
N, K = map(int, sys.stdin.readline().split())

# W: 물건의 무게, V: 물건의 가치
elements = list([0] * (N+1))
elements[0] = (0, 0)
for i in range(1, N+1):
    W, V = map(int, sys.stdin.readline().split())
    elements[i] = (W, V)

elements.sort(key=lambda x: x[0])
# print(elements)


dp = list([0] * (K+1) for _ in range(N+1))
# print(dp)

for i in range(1, N+1):
    for j in range(1, K+1):
        # 배낭의 허용 무게보다 넣을 무게가 크다면 i번째와 i+1번째의 넣은 무게를 같게한다.
        # 만약 허용 무게보다 작다면, 넣을 무게만큼 뺀 dp확인 후 현재 무게와 더하여 최대 값을 dp의 i번째에 저장한다.
        if j < elements[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-elements[i][0]] + elements[i][1])

print(max(dp[N]))