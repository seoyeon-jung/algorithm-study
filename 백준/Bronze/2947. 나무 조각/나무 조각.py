# 대소 관계 비교해서 단순 정렬

import sys
input = sys.stdin.readline

num = list(map(int, input().split())) # 숫자 리스트로 정렬

for i in range(len(num)-1):
    for j in range(0, len(num) - (i+1)):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j] # 순서 바꾸기
            print(*num)