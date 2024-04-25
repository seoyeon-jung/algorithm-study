import sys

n = int(sys.stdin.readline())
stack, score = [], 0

for _ in range(n):
    task = list(map(int, sys.stdin.readline().split()))

    if task[0] == 1:
        if task[2] - 1 == 0: # 1분짜리 과제인 경우
            score += task[1] # 바로 score에 저장
        else: # 점수와 시간을 -1 해서 저장
            stack.append([task[1], task[2] - 1])
    elif stack: # 첫 요소가 0인 경우
        stack[-1][1] -= 1
        if stack[-1][1] == 0:
            score += stack[-1][0]
            stack.pop()

print(score)