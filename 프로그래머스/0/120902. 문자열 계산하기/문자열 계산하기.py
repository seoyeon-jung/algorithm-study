def solution(my_string):
    lst = my_string.split(" ")
    answer = int(lst[0])
    op = None
    
    for el in lst[1:]:
        if el in ["+", "-"]:
            op = el
        else:
            if op == "+":
                answer += int(el)
            elif op == "-":
                answer -= int(el)
    
    return answer