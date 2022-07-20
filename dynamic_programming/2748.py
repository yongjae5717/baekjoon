import sys


def fib(n, memo):
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]
    else:
        return memo[n]


N = int(sys.stdin.readline())
memo = dict()
memo[0], memo[1], memo[2] = 0, 1, 1
result = fib(N, memo)
print(result)