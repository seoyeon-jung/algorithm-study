import math

N, S = map(int, input().split())
A = list(map(int, input().split()))

# 동생들 위치와 내 위치 차이의 절댓값을 리스트에 넣기
# set으로 중복 방지
arr = list(set(abs(A[i] - S) for i in range(N)))

# min
min_num = min(arr)

for i in range(len(arr)):
    # 제일 작은 수를 기준으로 최대 공약수를 얻는다
    min_num = math.gcd(arr[i], min_num)

print(min_num)
