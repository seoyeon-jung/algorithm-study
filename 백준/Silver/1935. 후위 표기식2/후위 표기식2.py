N = int(input()) # 피연산자의 개수
sen = input() # 후위 표기식
alpha = [0] * N # 피연산자에 대응하는 값 받을 리스트

# 연산인 경우에는 push, 아니면 pop


# 값 입력받기
for i in range(N):
    alpha[i] = int(input())

stack = [] # 스택

for i in sen:
    # A~Z 사이인 경우
    if 'A' <= i <= 'Z':
        stack.append(alpha[ord(i) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1+str2)
        elif i == '-':
            stack.append(str1-str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

# 소수점 둘째자리까지 출력
print('%.2f' % stack[0])