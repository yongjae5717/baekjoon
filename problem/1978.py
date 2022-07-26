import sys
input = sys.stdin.readline


def is_prime_number(number):
    if number <= 1:
        return False

    if number % 2 == 0:
        if number == 2:
            return True
        return False

    for i in range(3, int(pow(number, 0.5)) + 1, 2):
        if number % i == 0:
            return False
    return True


n = int(input())
lst = list(map(int, input().split()))
result = 0
for i in lst:
    if is_prime_number(i):
        result += 1

print(result)