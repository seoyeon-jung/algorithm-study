n = int(input()) # 사람의 수
arr = list(map(int, input().split()))
ans = [0] * n
for p in range(1, n+1):
    t = arr[p-1]
    cnt = 0
    for i in range(n):
        if cnt == t and ans[i] == 0:
            ans[i] = p
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)