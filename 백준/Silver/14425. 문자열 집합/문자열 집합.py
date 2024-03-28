import sys

N, M = map(int, sys.stdin.readline().split())
S = set([sys.stdin.readline().strip() for _ in range(N)])
count = 0

# 나열된 문자엳들 돌면서 S에 포함되어있는지 확인
for _ in range(M):
    check_word = sys.stdin.readline().strip()
    if check_word in S:
        count += 1

print(count)