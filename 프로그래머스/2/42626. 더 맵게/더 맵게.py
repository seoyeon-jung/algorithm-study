import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        new_arr = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_arr)
        answer += 1
        if scoville[0] < K and len(scoville) == 1:
            return -1
    return answer