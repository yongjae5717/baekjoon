import sys

N = int(sys.stdin.readline())

temp = N
temp2 = N
count, count2 = 0, 0


def issquare(n):
    return int(n ** 0.5) ** 2 == n


while True:
    if issquare(temp):
        break
    temp -= 1
    count += 1

while True:
    if issquare(temp2):
        break
    temp2 += 1
    count2 += 1


print(temp, temp2)

print(count, count2)