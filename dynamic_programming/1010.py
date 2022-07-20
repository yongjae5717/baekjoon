import sys


def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    # M >= N
    # Combination
    ans = int(factorial(M) / (factorial(N) * factorial(M-N)))
    print(ans)