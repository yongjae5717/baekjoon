"""
LCS: 최장 공통 부분 수열
ex)
ACAYKP, CAPCAK -> ACAK
output: LCS의 길이
"""

import sys

str1 = "0" + sys.stdin.readline().strip()
str2 = "0" + sys.stdin.readline().strip()

LCS = list([0] * len(str2) for _ in range(len(str1)))
for i in range(len(str1)):
    for j in range(len(str2)):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif str1[i] == str2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])


# for i in LCS:
#     print(i)

print(LCS[len(str1)-1][len(str2)-1])