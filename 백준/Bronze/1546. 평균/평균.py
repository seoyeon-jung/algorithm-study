N = input()
score_list = list(map(int, input().split()))
max_score = max(score_list)

sum_score = sum(score_list)

print(sum_score * 100 / max_score / int(N))

# 최댓값 구하기
# 모든 점수를 '점수 / 최댓값 * 100' 으로 고치기
# 바뀐 점수들의 평균값 출력

