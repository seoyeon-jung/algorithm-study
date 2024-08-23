from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) # 명령의 수

# push X : X를 큐에 넣기
# pop : 가장 앞에 있는 정수를 빼고 그 수를 출력 (없으면 -1 출력)
# size : 정수의 개수 출력
# empty : 비어있으면 1, 아니면 0 출력
# front : 가장 앞에 있는 정수 출력 (없으면 -1 출력)
# back : 가장 뒤에 있는 정수 출력 (없으면 -1 출력)

q = deque()

for i in range(N): # 명령의 수만큼 반복
    quiz = list(input().split())

    if quiz[0] == 'push':
        q.append(quiz[1])
    elif quiz[0] == 'pop':
        if len(q) > 0:
            temp = q.popleft()
            print(temp)
        else:
            print(-1)
    elif quiz[0] == 'size':
        print(len(q))
    elif quiz[0] == 'empty':
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif quiz[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif quiz[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)