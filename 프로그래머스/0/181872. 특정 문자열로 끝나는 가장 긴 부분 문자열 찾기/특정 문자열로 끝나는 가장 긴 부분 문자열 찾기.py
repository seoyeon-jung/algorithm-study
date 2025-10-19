def solution(myString, pat):
    answer = ''
    last = myString.rfind(pat)
    if last != -1:
        answer = myString[:last+len(pat)]
    return answer