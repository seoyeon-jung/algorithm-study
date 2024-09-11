n = list(map(int, str(input()))) # 각 자리수 리스트로 계산
n.sort(reverse=True) # 내림차순 정렬 

for i in n:
    print(i, end='')