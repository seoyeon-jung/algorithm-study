def solution(board, k):
    result = 0
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            if i + j <= k:
                result += board[i][j]
                
    return result