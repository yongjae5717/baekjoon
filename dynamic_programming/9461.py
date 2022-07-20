import sys


def fib(n, memo):
    if n not in memo:
        memo[n] = fib(n-3, memo) + fib(n-2, memo)
        return memo[n]
    else:
        return memo[n]


memo = dict()
memo[1], memo[2], memo[3] = 1, 1, 1
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    result = fib(N, memo)
    print(result)