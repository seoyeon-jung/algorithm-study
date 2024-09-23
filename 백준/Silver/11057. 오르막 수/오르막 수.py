# 끝의 수 i는 N-1일 때 i에 i-1을 더하면 끝의 수가 i일때 만들 수 있는 오르막 수 개수 구할 수 있음
# 끝의 수 0~9까지 dp를 저장하는 리스트를 만들면 된다
# 이전 dp에 i-1만 더해주면 새로운 N의 끝의 수들을 업데이트 가능
# 오르막 개수 >> dp를 전부 더하고 10007로 나누어 출력

import sys
input = sys.stdin.readline

N = int(input())
dp = [1] * 10

for i in range(N-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp) % 10007)