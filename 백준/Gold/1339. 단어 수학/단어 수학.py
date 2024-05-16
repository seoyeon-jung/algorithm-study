# 알파벳을 숫자로 바꿀 떄 큰 수에 관해 경우의 수 생각하기
# 1. 같은 숫자 여러 개인 경우 생각
# 2. 자릿수 더해서 가장 큰 자릿수부터 9 8 7 ...

import sys

N = int(sys.stdin.readline())
S = [sys.stdin.readline().strip() for _ in range(N)]

words = {}  #단어별 값을 지정해야 함

for s in S:
    x = len(s) - 1 #자릿수 구하기 위한 계산
    for i in s:
        if i in words:
            words[i] += 10**x #x만큼 제곱한걸 더하기
        else:
            words[i] = 10**x #x만큼 제곱해서 넣기
        x -=1

words_sorted = sorted(words.values(), reverse=True) # value 내림차순으로
result = 0
num = 9

for k in words_sorted:
    result += k * num #내림차순 순으로 9부터 곱해서 더하기
    num -= 1

print(result)