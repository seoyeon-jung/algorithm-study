# 반경이 서로 다른 n개의 원판
# 반경 큰 순서대로 쌓여있어야 함

N = int(input()) # 원판 개수

# 하나도 없는 경우 > 그냥 넘어감
# 원판 1개 > 3번으로 옮김
# 원판 3개 > 1번 -> 2번 / 2번 -> 3번 / 1번 -> 2번
# => 재귀

# 가장 큰 원판 제외 나머지 원판을 2번 기둥으로 이동
# 가장 큰 원판은 3번
# 나머지는 3번
# 계속 반복하기

def hanoi(num, start, end):
    if num == 1:
        print(start, end)
        return
    else:
        hanoi(num-1, start, 6 - start - end)
        print(start, end)
        hanoi(num-1, 6-start-end, end)

print(2**N - 1)
hanoi(N, 1, 3)