"""
T: 테스트 케이스의 수
N: 배열의 크기 (1 <= N <= 1000)
N 다음줄에는 배열

X의 maximum subarray의 합을 구한다.
"""

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))

    ans = -10000001
    for i in range(1, N+1):
        result = sum(lst[:i])
        if ans < result:
            ans = result
        for j in range(1, N-i+1):
            result = result - lst[j-1] + lst[j+i-1]
            if ans < result:
                ans = result

    print(ans)