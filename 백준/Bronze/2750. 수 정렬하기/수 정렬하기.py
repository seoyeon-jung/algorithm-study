N = int(input()) # 수의 개수
num = []

for i in range(N):
    num.append(int(input())) # N개만큼 숫자 입력

answer = sorted(num) # 오름차순으로 정렬

for i in range(len(num)):
    print(answer[i])