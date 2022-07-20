import sys

N = int(sys.stdin.readline())

count = 0
result = 0
lst = list([0] * (N + 1))
for i in range(2, N + 1):
    result = lst[i-1] + 1
    if i % 2 == 0:
        result = min(result, lst[i // 2] + 1)
    if i % 3 == 0:
        result = min(result, lst[i // 3] + 1)
    lst[i] = result
print(lst[N])