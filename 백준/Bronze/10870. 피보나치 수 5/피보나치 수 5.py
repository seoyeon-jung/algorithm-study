# 반복해서 피보나치 합 구하기
# n = 0인 경우 0, 1인 경우 1

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))