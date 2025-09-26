def solution(i, j, k):
    answer = 0
    num = ''
    for u in range(i, j+1):
        num += str(u)
    for f in num:
        if f == str(k):
            answer += 1
    return answer