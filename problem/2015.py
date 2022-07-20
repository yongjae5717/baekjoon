"""
N: 1~200,000
K: 2,000,000,000

N개의 수열이 주어지는데, 부분합이 K인 개수를 구하는 프로그램
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))
memo = {0: 1}
sum_value = 0
result = 0

for val in lst:
    sum_value += val

    # 이전 누적값에서 - K인 것이 존재한다면 result에 추가해줌
    if sum_value - K in memo.keys():
        result += memo[sum_value-K]

    if sum_value not in memo.keys():
        memo[sum_value] = 1
    else:
        memo[sum_value] += 1

print(result)
# print(memo)