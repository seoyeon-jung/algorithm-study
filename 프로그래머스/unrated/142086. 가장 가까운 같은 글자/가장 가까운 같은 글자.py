def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[0:i]:
            answer.append(i - s[0:i].rindex(s[i]))
            # rindex: 뒤에서부터 index 구함
        else:
            answer.append(-1)
    return answer