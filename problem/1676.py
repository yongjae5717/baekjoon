import sys

N = int(sys.stdin.readline())

num = 1
if N == 0 or N == 1:
    print(0)
else:
    for i in range(1, N+1):
        num *= i

    st = str(num)

    count = 0
    for i in range(len(st)):
        if st[len(st)-i-1] == "0":
            count += 1
        else:
            break
    print(count)