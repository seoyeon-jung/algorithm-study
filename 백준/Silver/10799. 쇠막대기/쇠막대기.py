test = input()
stack = []
answer = 0

for i in range(len(test)):
    # 열린 괄호는 계속 추가
    if test[i] == '(':
        stack.append('(')
    # 닫는 괄호인 경우는 pop
    else:
        # 레이저인 경우
        if test[i-1] == '(':
            stack.pop()
            answer += len(stack)
        # 막대의 끝인 경우
        else:
            stack.pop()
            answer += 1

print(answer)