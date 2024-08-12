# 1 ~ 49 중 수 6개 고르기
# k 개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택
# 경우의 수를 모두 출력해야 한다

# k(숫자 개수), k만큼 숫자 입력(집합 S에 포함된다)

# 6개 뽑아서 출력해야 한다

import sys

input = sys.stdin.readline

def dfs(dep, i):
    if dep == 6:
        print(*ret)
        return
    
    for i in range(i, k):
        # 최종 길이리를 만족하지 못하는 경우
        if dep + k - i < 6:
            return #그냥 종료
        ret.append(s[i]) # 만족하는 경우에만 append
        dfs(dep+1, i+1) # 반복
        ret.pop() # 다음 요소 탐색을 위한 pop

while True:
    g = list(map(int, input().split()))
    k = g[0]
    s = g[1:]
    if k == 0:
        break
    ret = []
    dfs(0, 0)
    print()