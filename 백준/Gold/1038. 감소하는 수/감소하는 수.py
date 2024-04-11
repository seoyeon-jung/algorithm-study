# 자릿수가 가장 큰 자릿수부터 감소 => 감소하는 수
# N번째 감소하는 수를 출력 (없으면 -1)
import sys
from itertools import combinations

N = int(sys.stdin.readline()) # n번째 감소하는 수 출력

# for문으로 반복문 돌면서 감소하는 수 찾기
# 감소하는 수 최대 9876543210

# 조합 사용하기

result = [] # 감소하는 수 list
for i in range(1, 11):
    for j in combinations(range(10), i): # 0~9 하나씩 조합 만들기
        num = ''.join(list(map(str, reversed(list(j)))))
        result.append(int(num))

result.sort() # 오름차순 정렬

if N >= len(result):
	print(-1)
else:
	print(result[N])