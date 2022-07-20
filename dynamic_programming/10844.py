import sys

N = int(sys.stdin.readline())

# 1 > 9 [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 2 > 17 [12, 23, 34, 45, 56, 67, 78, 89, 98, 87, 76, 65, 54, 43, 32, 21, 10]
# 3 > 32 [101, 123, 121, 212, 210, 234, 232, 321, 323, 345, 343, 432, 434, 456,

memo = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(N-1):
    temp = [0] * 10
    for i in range(10):
        if i > 0:
            temp[i - 1] += memo[i]
        if i < 9:
            temp[i + 1] += memo[i]
    memo = temp

result = sum(memo) % 1000000000
print(result)