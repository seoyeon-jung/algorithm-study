n = int(input())

# 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력

arr = []

def dfs():
    # 순열 길이가 n인 경우
    if len(arr) == n:
        print(*arr)
        return
    # 순열 만들기
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop() # i를 넣기 전의 상태로 돌아가기 위해 pop

dfs()