N, M = map(int, input().split())
S = set([input() for _ in range(N)])
count = 0

for _ in range(M):
    check = input()
    if check in S:
        count += 1

print(count)