from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
position = list(map(int, input().split())) # 뽑아내려는 수의 위치
q = deque([i for i in range(1, N+1)])

count = 0

for i in position:
    while True:
        # 인덱스 첫번재가 뽑아내려는 수의 위치가 동일한 경우
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) < len(q) / 2:
                # 반복 (위치가 동일할 때까지)
                while q[0] != i:
                    q.append(q.popleft())
                    count += 1
            else:
                # 반으로 나눈 것보다 클 때
                while q[0] != i:
                    q.appendleft(q.pop())
                    count += 1

print(count)