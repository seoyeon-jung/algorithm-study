# 총금액 X
# 구매한 물건의 종류 N
# 가격 a 개수 b => a * b
# 물건 가격과 총 금액 일치 = Yes

X = int(input())
N = int(input())

sum = 0

for i in range(N):
    price, count = map(int, input().split())
    sum += (price * count)

if X == sum:
    print('Yes')
else:
    print('No')