# XXXX -> AAAA로 대체
# XX -> BB로 대체
# 'X'가 남아있는 경우에는 보드를 덮을 수 없으면 -1 출력
# replace 사용

import sys

input = sys.stdin.readline

board = input()
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)