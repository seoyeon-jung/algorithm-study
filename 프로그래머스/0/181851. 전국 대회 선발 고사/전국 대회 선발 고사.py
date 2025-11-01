def solution(rank, attendance):
    rank_arr = []
    
    for i in range(len(rank)):
        if attendance[i]:
            rank_arr.append([rank[i], i])
            
    rank_arr.sort(key = lambda v : v[0])
    return 10000 * rank_arr[0][1] + 100 * rank_arr[1][1] + rank_arr[2][1]