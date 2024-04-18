# a, b, c (c가 가득 차있음)
# 물을 한 번 옮겨담는 경우 => 경우의 수 6가지 있음
# bfs로 완전탐색 구현
# 물은 어차피 c로 정해져 있음
# c 전체(z) = a(x) + b(y) + c(Z)
# 방문했음을 체크해서 중복 방지

import sys
from collections import deque

# x, y 경우의 수 저장하는 함수
def check_visited(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

# bfs
def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y

        # a 물통이 비어있으면 c 물통에 남아있는 양 저장
        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, b - y)
        check_visited(x - water, y + water)

        # x -> z
        water = min(x, c - z)
        check_visited(x - water, y)

        # y -> x
        water = min(y, a - x)
        check_visited(x + water, y - water)

        # y -> z
        water = min(y, c - z)
        check_visited(x, y - water)

        # z -> x
        water = min(z, a - x)
        check_visited(x + water, y)

        # z -> y
        water = min(z, b - y)
        check_visited(x, y + water)

# a, b, c 입력
a, b, c = map(int, sys.stdin.readline().split())

# 경우의 수를 담을 큐
q = deque()
q.append((0, 0)) # 초기

# 방문 여부
visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True

# 답을 저장할 배열
answer = []

bfs()

answer.sort()
for i in answer:
    print(i, end = " ")