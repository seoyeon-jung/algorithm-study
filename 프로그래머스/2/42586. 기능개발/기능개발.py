def solution(progresses, speeds):
    # progresses[0]이 먼저 배포되어야만 다음 것 배포 가능
    answer = []
    days = 0 # 배포날 계산
    cnt = 0 # 완료된 기능
    
    # 리스트 len만큼 반복
    while len(progresses) > 0:
        if(progresses[0] + days * speeds[0]) >= 100:
            # 배포되기 때문에 리스트에서 제거
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0: # 완료된 기능이 있는 경우
                answer.append(cnt)
                cnt = 0
            else: # 완료된 기능이 없다면 day + 1
                days += 1
    answer.append(cnt)
    return answer