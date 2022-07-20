import sys
# 재귀 함수의 제한 범위를 늘려주는 방법
sys.setrecursionlimit(10**6)

num = int(sys.stdin.readline())
memo = dict()


def cal(N, dictionary):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        if N not in dictionary:
            dictionary[N] = cal(N-1, dictionary) + 2 * cal(N-2, dictionary)
            return dictionary[N]
        else:
            return dictionary[N]


result = cal(num, memo) % 10007
print(result)