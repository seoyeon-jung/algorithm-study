# nCm 을 계산하면 된다
# n! / (n-m)! * m! >> 계산하면 끝

# 팩토리얼 계산 (1부터 N까지 계속 곱한다)
def fact(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

n, m = map(int, input().split())
answer = fact(n)//(fact(n - m) * fact(m))

print(answer)