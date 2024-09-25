N = int(input())
dp = []

# 이차원리스트 형태로 dp에 저장
for i in range(N):
    dp.append(list(map(int, input().split())))

# 행 기준
for i in range(1, N):
    # 열 기준
    for j in range(0, i+1):
        if j == 0:
            # 0열끼리 더하기
            dp[i][0] += dp[i-1][0]
        elif j == i:
            # 마지막 열끼리 더하기
            dp[i][j] += dp[i-1][j-1]
        else:
            # 더 큰 경우 더하기
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1])) # n-1 행에서 최댓값 출력