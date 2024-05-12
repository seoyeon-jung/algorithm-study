N = int(input())
num = []

for i in range(N):
    num.append(int(input()))
answer = sorted(num)

for i in range(len(num)):
    print(answer[i])