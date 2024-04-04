# 정수 n
# n개의 줄에 d(과제 마감일), w(과제의 점수)
# 얻을 수 있는 최대값 print

import heapq

n = int(input())
hq = []
max_day = 0

for i in range(n):
    d, w = map(int, input().split())
    heapq.heappush(hq, (-w, d))
    if max_day < d:
        max_day = d

finished = [False] * (max_day + 1)
score = 0

while hq:
    # 가장 높은 순으로
    w, d = heapq.heappop(hq)
    w = -w
    # d일부터 1일까지 거꾸로 돌기
    for i in range(d, 0, -1):
        if finished[i]:
            continue

        finished[i] = True
        score += w
        break

print(score)

# 점수가 높은 순으로 처리
# 그 날짜에 다른 작업 있으면 바로 전날에 배정
# 위 과정 반복

# max heap 구성
# heap이 빌때까지 위의 과정 반복
# 현재 점수 가장 높은 과제 - 마감일부터 비어있는 날 찾기 - 비어있는 날에 배정