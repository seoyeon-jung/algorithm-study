import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()

for i in range(N):
    question = input().split()

    if question[0] == 'push_front':
        q.appendleft(question[1])
        
    if question[0] == 'push_back':
        q.append(question[1])
        
    if question[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    if question[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())

    if question[0] == 'size':
        print(len(q))
    
    if question[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    
    if question[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    
    if question[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])