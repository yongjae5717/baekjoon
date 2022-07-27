import sys
input = sys.stdin.readline

n = int(input())
# 입력 리스트
a = list(map(int, input().split()))
# 누적합 구하기
s = list()
s.append(a[0])
for i in range(1, n):
    s.append(s[i-1] + a[i])

m = int(input())

for i in range(m):
    start, end = map(int, input().split())
    if start == 1:
        print(s[end-1])
    else:
        print(s[end-1] - s[start-2])