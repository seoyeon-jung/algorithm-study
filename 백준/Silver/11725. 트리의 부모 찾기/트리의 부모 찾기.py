import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

ans = [0] * (N+1)

def bfs():
    while q:
        current = q.popleft()
        for i in graph[current]:
            if ans[i] == 0:
                ans[i] = current
                q.append(i)

bfs()
res = ans[2:]
for x in res:
    print(x)