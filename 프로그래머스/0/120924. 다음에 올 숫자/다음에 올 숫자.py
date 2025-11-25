def solution(common):
    x, y, z = common[:3]
    if y - x == z - y:
        answer = common[-1] + (y - x)
    elif y // x == z // y:
        answer = common[-1] * (y // x)
    return answer