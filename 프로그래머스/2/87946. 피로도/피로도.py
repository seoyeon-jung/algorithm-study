from itertools import permutations

def solution(k, dungeons):
    # k = 현재 피로도
    # 최소 필요 피로도: 던전 전 피로도
    # 소모 피로도: 던전 후 소모된 피로도
    # dungeons[0]부터 순서 바꿔가며 피로도 계산
    # 최대로 돌 수 있는 던전 횟수를 return
    # 순열 이용
    
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        count = 0
        
        for need, spend in p:
            if tmp >= need:
                tmp -= spend
                count += 1
        answer = max(answer, count)
            
    return answer