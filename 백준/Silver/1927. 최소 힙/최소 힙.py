import sys
import heapq

input = sys.stdin.readline

N = int(input()) # 연산의 개수
min_heap = [] # 연산 넣을 배열

for _ in range(N):
    num = int(input()) # 숫자 입력

    if num == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap)) # 가장 작은 원소 출력
        else:
            print(0)
    else:
        heapq.heappush(min_heap, num)