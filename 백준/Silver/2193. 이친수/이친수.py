import sys
input = sys.stdin.readline

N = int(input())

# N자리수만큼 dp 테이블 생성
dp = [0] * (N+1)
dp[1] = 1 # 한자리 수이면 무조건 1  (0으로 시작하지 않음)

for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N])