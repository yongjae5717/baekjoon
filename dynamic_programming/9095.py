import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    lst = []
    if N > 0:
        lst.append(1)
    if N > 1:
        lst.append(2)
    if N > 2:
        lst.append(4)
    for i in range(3, N):
        lst.append(sum(lst[i-3:i]))

    print(lst[N-1])
