def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    answer = sum(int(i) for i in s.split())
    return answer