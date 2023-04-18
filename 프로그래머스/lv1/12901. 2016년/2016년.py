def solution(a, b):
    # 2016년은 윤년 (2월 29일까지 있음)
    # a월 b일은 실제 있는 날
    day = ('FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU')
    month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    answer = day[(sum(month[:a-1])+b-1)%7] 
    return answer