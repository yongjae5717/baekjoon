import sys

T = int(sys.stdin.readline())

zero = [1, 0, 1]
one = [0, 1, 1]


def fib(N):
    length = len(zero)
    if length <= N:
        for i in range(length, N+1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[N], one[N])


for _ in range(T):
    N = int(sys.stdin.readline())
    fib(N)