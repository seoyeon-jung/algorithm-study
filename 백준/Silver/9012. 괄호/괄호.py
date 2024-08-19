t = int(input()) # 테스트 케이스

# NO인 경우를 생각
# ()) 인 경우
# ( 개수와 ) 개수가 다를 때

for i in range(t):
    string = list(input())
    # 짝을 맞는지 안 맞는지 여부를 알기 위한 변수
    sum = 0

    for j in range(len(string)):
        if string[j] == "(":
            sum += 1
        else:
            sum -= 1
        
        if sum < 0: # ())인 경우
            print("NO")
            break

    if sum > 0: # 짝이 맞지 않는 경우
        print("NO")
    elif sum == 0: # 짝이 맞으면 sum이 0
        print("YES")