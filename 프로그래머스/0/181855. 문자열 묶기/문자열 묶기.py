def solution(strArr):
    lst = [len(i) for i in strArr]
    tmp = []
    for i in set(lst):
        tmp.append(lst.count(i))
    return max(tmp)