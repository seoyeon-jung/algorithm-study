import sys
input = sys.stdin.readline


N, M = map(int, input().split()) # 배열의 데이터 수, 횟수 입력받기
num_list = list(map(int, input().split())) # 숫자 리스트 입력받기
sum = [0]
tmp = 0

# 누적 합 구하기
for i in num_list:
    tmp = tmp + i
    sum.append(tmp)

# 구간 합 구하기
for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])