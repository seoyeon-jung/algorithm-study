def solution(score):
    avg = [sum(s)/len(s) for s in score]
    sorted_avg = sorted(avg, reverse=True)
    grade = []
    for i in avg:
        grade.append(sorted_avg.index(i) + 1)
    return grade