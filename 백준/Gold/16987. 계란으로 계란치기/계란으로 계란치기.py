n = int(input())
egg_list = []

for _ in range(n):
    s, w = map(int, input().split())
    egg_list.append([s, w])

answer = 0

def crackedEgg(sequence):
    global answer
    if sequence == n:
        count = 0
        for i in range(n):
            if egg_list[i][0] <= 0:
                count += 1
        answer = max(count, answer)
        return
    
    # 손에 있는 계란이 깨지면 다른 계란 선택
    if egg_list[sequence][0] <= 0:
        crackedEgg(sequence + 1)
        return
    
    checkEgg = True # 계란이 모두 깨졌는가

    for i in range(n):
        if i == sequence:
            continue
        if egg_list[i][0] > 0:
            checkEgg = False
            break

    # 다 깨져 있는 경우 종료
    if checkEgg:
        answer = max(answer, n - 1)
        return
    
    # 계란 치기
    for i in range(n):
        if i == sequence: continue
        if egg_list[i][0] <= 0:
            continue

         # 계란 치기
        egg_list[sequence][0] -= egg_list[i][1]
        egg_list[i][0] -= egg_list[sequence][1]
        crackedEgg(sequence + 1)

        # 깨지지 않은 경우 다시 복구
        egg_list[sequence][0] += egg_list[i][1]
        egg_list[i][0] += egg_list[sequence][1]

crackedEgg(0) # index[0] 부터 시작
print(answer)