# k번째 사람을 제거
# 나머지 사람들은 다시 원을 만들어서 위 과정 반복
# 사람들 제거되는 순서 <> 안에 추가해서 출력하기

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
result = []

for i in range(1, N+1):
    q.append(i)

while q:
    for i in range(K - 1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<", end='')
print(', '.join(map(str,result)), end='')
print(">")