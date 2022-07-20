import sys

array = list(map(int, sys.stdin.readline().split()))
if array[0] == array[1] == array[2]:
    print(10000 + array[0] * 1000)
elif array[0] == array[1] != array[2]:
    print(1000 + array[0] * 100)
elif array[0] != array[1] == array[2]:
    print(1000 + array[1] * 100)
elif array[0] == array[2] != array[1]:
    print(1000 + array[0] * 100)
else:
    print(max(array) * 100)
