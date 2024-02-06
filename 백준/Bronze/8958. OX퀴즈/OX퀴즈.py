N = int(input())

for i in range(N):
    x = input()
    score = 0
    score_sum = 0
    for j in x:
        if j == 'O':
            score += 1
        else:
            score = 0
        score_sum += score
    print(score_sum)