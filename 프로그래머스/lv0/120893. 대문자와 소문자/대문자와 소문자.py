def solution(my_string):
    answer = ''
    
    for x in my_string:
        if x.isupper():  # 대문자인 경우
            answer += x.lower()  # 소문자로 변경
        else:
            answer += x.upper()  # 소문자인 경우 대문자로 변경
            
    return answer