# 정수 k
k = int(input())

# k줄에 정수 1개씩 주어짐
numArr = [] # 최종적으로 더할 숫자들의 list

for i in range(k):
    num = int(input()) # k줄만큼 숫자 입력해야 함
    # 잘못된 수를 부를 때마다 0 (가장 최근 수 삭제)
    if num == 0:
        numArr.pop()
    else:
        numArr.append(num)

# 모든 수의 합을 출력
print(sum(numArr))