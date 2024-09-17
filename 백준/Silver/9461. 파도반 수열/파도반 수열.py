# n번째 정삼각형 변의 길이 = n-2 삼각형 변 길이 + n-3 삼각형 변 길이

import sys
input = sys.stdin.readline

arr = [0, 1, 1, 1] + [0 for i in range(97)] # 3번째 삼각형의 변의 길이
# 나머지 97개는 -

def solution(n):
    if arr[n]:
        return arr[n]
    else:
        arr[n] = solution(n-2) + solution(n-3)
        return arr[n]
    
T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))