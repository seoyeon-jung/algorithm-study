from itertools import permutations

def solution(numbers):
    answer = []
    # 각 숫자 분리
    nums = [n for n in numbers]
    
    # 각 숫자로 여러 조합해보기 (순열조합 이용)
    nums_arr = []
    for i in range(1, len(numbers) + 1):
        nums_arr += list(permutations(nums, i))
        
    # 순열조합들을 하나의 int형 숫자로 변환
    new_nums = [int(("").join(p)) for p in nums_arr]
    
    # 조합 중 소수인 것들만 answer++
    for n in new_nums:
        # 2보다 작은 경우 소수 아님
        if n < 2:
            continue
        check = True
        # n의 제곱근보다 작은 숫자까지만 계산
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                check = False
                break
        if check: # 소수인 경우
            answer.append(n)
            
    # set 통해 중복 제거 후 반환
    return len(set(answer))