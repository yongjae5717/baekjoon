import sys
input = sys.stdin.readline


a, b = map(int, input().split())
result = 0
array = [True for _ in range(int(pow(b, 0.5)) + 1)]

for i in range(2, int(pow(b, 0.5)) + 1):
    if array[i]:
        j = 2
        while i * j <= int(pow(b, 0.5)):
            array[i * j] = False
            j += 1

for i in range(2, int(pow(b, 0.5))+1):
    if array[i]:
        count = 1
        while True:
            count += 1
            if a <= pow(i, count) <= b:
                result += 1
            if pow(i, count) > b:
                break

print(result)