"""
스티커 2n개 구매 -> 2행 N열로 배치
스티커 1장을 떼면 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용불가 (상하좌우 스티커 사용 불가)
모든 스티커가 붙일 수 없는 상황이 되었을때, 각 스티커의 점수 최대의 합을 구하는 프로그램

모든 스티커가 찢어지기 위해서는 좌표 (0, 0)에서는 (1, 1) 또는 (2, 1)으로 가야한다.
그러므로 y 좌표가 0이라면 (x, 0) -> (x+1, 1) or (x+2, 1)
그리고 y 좌표가 1이라면 (x, 1) -> (x+1, 0) or (x+2, 0)으로 이동해야한다.
"""

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())

    # sticker 선언 밑 점수 입력
    stickers = list()
    for _ in range(2):
        stickers.append([0] + list(map(int, sys.stdin.readline().split())))
    # print("\n")
    # print("original stickers")
    # for i in stickers:
    #     print(i)
    if N == 1:
        print(max(stickers[0][1], stickers[1][1]))
    else:
        # dp 초기화
        dp = list([0] * (N+1) for _ in range(2))
        dp[0][1] = stickers[0][1]
        dp[1][1] = stickers[1][1]

        for i in range(1, N+1):
            # case1: (0, 1)에서 시작할 경우
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + stickers[0][i]
            # case2: (0, 0)에서 시작할 경우
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + stickers[1][i]

        # print("dp")
        # for j in dp:
        #     print(j)
        print(max(dp[0][N], dp[1][N]))