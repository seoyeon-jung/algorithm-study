def solution(n, slicer, num_list):
    num1, num2, num3 = slicer
    if n == 1: return num_list[:num2+1]
    if n == 2: return num_list[num1:]
    if n == 3: return num_list[num1:num2+1]
    return num_list[num1:num2+1:num3]