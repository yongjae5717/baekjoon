import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * 100001
start, result = 0, 0

for i in range(n):
    count[a[i]] += 1
    # a[i]를 포함 시켰을 때, 제한된 크기인 k보다 클 경우에 처음 나왔던 a[i]와 동일한 수 까지 빼주기
    while count[a[i]] > k:
        count[a[start]] -= 1
        start += 1
    # 최장 부분 수열의 개수가 큰 것을 고르는 과정
    result = max(result, i - start + 1)

# 결과 출력
print(result)