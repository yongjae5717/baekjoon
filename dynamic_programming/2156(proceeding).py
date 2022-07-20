import sys

N = int(sys.stdin.readline())
array = [0] + list(int(sys.stdin.readline()) for i in range(N))
# print(array)
if N < 3:
    print(sum(array))
else:
    memo = [0] * (N + 1)
    memo[1] = array[1]
    memo[2] = array[1] + array[2]
    # 앞잔 2잔 마신 경우
    # 바로 앞잔 마신 경우
    # 바로 앞잔을 안마신 경우
    for i in range(3, N+1):
        memo[i] = max(memo[i-1], array[i-1] + array[i] + memo[i-3], memo[i-2] + array[i])
    print(memo[N])