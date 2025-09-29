def solution(myString):
    answer = [word.strip() for word in myString.split('x') if word.strip()]
    answer.sort()
    return answer