from collections import deque

def solution(n, computers):
    def BFS(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visited[i] = 1
            for connect in range(n):
                if computers[i][connect] and not visited[connect]:
                    q.append(connect)
    
    answer = 0
    visited= [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1
            
    return answer