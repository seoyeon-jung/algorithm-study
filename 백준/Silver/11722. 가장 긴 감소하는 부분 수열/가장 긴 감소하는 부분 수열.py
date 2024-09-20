# 수열 중에서 가장 긴 감소하는 부분 구하기
# 각 숫자를 비교하면서 줄어드는 부분 확인

# dp를 배열 크기만큼 1로 초기화
# 이중 반복문으로 현재 위치와 그 앞의 수들을 비교
# 앞의 수가 현재 위치보다 클 때 앞의 수에 해당하는 dp 값과 현재 위치의 dp값을 비교
# >> 큰 값을 현재 위치 dp에 넣는다
# dp 리스트 중 가장 큰 값 출력

n = int(input())
num_list = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(0, i):
        if num_list[i] < num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))