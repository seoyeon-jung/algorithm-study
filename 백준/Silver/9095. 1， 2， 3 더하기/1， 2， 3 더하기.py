# f(n) = f(n-3)+f(n-2)+f(n-1) (n이 3보다 더 클 때)

import sys
input = sys.stdin.readline

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n-1) + solution(n-2) + solution(n-3)
    
T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))