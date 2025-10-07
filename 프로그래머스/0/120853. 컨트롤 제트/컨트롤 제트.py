def solution(s):
    num = s.split()
    
    for i, j in enumerate(num):
        if j == 'Z':
            num.pop(i-1)
    
    return sum([int(i) for i in num if i is not None and i.lstrip('-').isdigit()])