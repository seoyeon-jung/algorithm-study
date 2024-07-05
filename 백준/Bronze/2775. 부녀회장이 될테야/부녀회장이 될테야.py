# 0층 사람들은 정해져 있으므로 배열로 지정
# 아래층의 1~n호 합 구하기 반복 => 배열에 추가
# 배열에서 k층 n호 찾아서 출력

T = int(input()) # test case

for i in range(T): # test case만큼 반복
    k = int(input())
    n = int(input())

    people = [i for i in range (1, n + 1)] # 0층부터 1호~n호 사람 수 담기

    for j in range(k):
        for k in range(1, n):
            people[k] += people[k -1] # 아래층 1~n호 값 더하기

    print(people[-1])