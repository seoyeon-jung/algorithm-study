import heapq

def solution(operations):
    answer = []
    
    q = []
    # if문으로 세 가지 조건 맞게 찾아보기
    for operation in operations:
        x, num = operation.split() # 명령어, 데이터
        num = int(num)
        
        if x == 'I':
            heapq.heappush(q, num)
        elif x == 'D' and num == 1:
            if len(q) != 0:
                max_value = max(q)
                q.remove(max_value)
        elif x == 'D' and num == -1:
            if len(q) != 0:
                heapq.heappop(q)
    
    # 길이가 0인 경우는 [0, 0]
    if len(q) == 0:
        answer = [0, 0]
    else:
        answer = [max(q), heapq.heappop(q)]
        
    return answer