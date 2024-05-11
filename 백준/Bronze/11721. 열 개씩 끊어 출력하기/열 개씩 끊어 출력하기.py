N = str(input()) #문자형으로 입력받기
count = 0

for i in range(len(N)) :
    if count < 9 :
        print(N[i], end = "")
        count += 1
    elif count == 9 :
        print(N[i])
        count = 0