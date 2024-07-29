# 조합 이용해보기
from itertools import combinations

N, M = map(int, input().split())

numList = [i for i in range(1, N+1)]

for seq in combinations(numList, M):
    print(*seq)