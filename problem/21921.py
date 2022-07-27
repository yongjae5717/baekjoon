import sys
input = sys.stdin.readline

n, x = map(int, input().split())

visited_num = list(map(int, input().split()))

s = list()
temp = sum(visited_num[:x])
s.append(temp)
for i in range(n-x):
    temp = temp - visited_num[i] + visited_num[x + i]
    s.append(temp)

if max(s) == 0:
    print("SAD")
else:
    print(max(s))
    print(s.count(max(s)))