N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
count = -1

def dfs(v):
    visited[v] = True
    global count
    count += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(count)