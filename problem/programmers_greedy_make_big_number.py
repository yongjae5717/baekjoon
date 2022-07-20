def solution(number, k):
    result = list()

    for i in str(number):
        while result and result[-1] < i and k>0:
            result.pop()
            k -= 1
        result.append(i)

    if k:
        result=result[:-k]
    answer = ''.join(result)

    return answer
