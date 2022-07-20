"""
3020번 개똥벌레
N(짝수): 동굴의 길이
H: 동굴의 높이
종유석과 석순이 번갈아가면서 등장한다
종유석: 아래에서부터 등장
석순: 위에서부터 등장
"""

import sys

N, H = map(int, sys.stdin.readline().split())

up = [0] * (H+1)
down = [0] * (H+1)
count = [0] * (H+1)

for i in range(N):
    temp = int(sys.stdin.readline())
    if i % 2 == 0:
        down[temp] += 1
    else:
        up[H-temp+1] += 1

for j in range(H-1, 0, -1):
    down[j] += down[j+1]

for k in range(2, H+1):
    up[k] += up[k-1]

for s in range(1, H+1):
    count[s] = down[s] + up[s]

min_count = min(count[1:])
print(min_count, count[1:].count(min_count))