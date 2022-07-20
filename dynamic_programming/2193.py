import sys


def fib(N, memo):
    if N == 1 or N == 2:
        return 1
    elif N not in memo:
        temp = fib(N-2, memo) + fib(N-1, memo)
        memo[N] = temp
        return memo[N]
    else:
        return memo[N]


memo = dict()
N = int(sys.stdin.readline())
print(fib(N, memo))