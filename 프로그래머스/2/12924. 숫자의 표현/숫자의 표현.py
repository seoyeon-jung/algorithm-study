def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        num = 0
        for j in range(i, n + 1):
            num += j
            if num == n:
                cnt += 1
                break
            if num > n:
                break
    return cnt