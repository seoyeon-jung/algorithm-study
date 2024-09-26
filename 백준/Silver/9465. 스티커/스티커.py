# 지그재그로 가는 경우 2가지
# 건너뛰지 않고 계속 지그재그
# 한 칸 건너뛰면서 지그재크
# 두 가지를 비교해서 dp값 저장한 후에 최댓값을 구하기

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))