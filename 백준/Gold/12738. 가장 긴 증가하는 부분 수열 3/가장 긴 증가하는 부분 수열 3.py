# 긴 증가하는 부분수열 찾기

# for문으로 배열 끝까지 검사
# 현재값보다 큰 값이 있다면 바로 수열에 추가
# => 이분탐색으로 찾기
# 그 수열 길이를 출력

n = int(input())
n_list = list(map(int, input().split(' ')))

def binary_search(start, end, target):
    if start > end:
        return start
    
    mid = (start + end) // 2

    if result[mid] > target:
        return binary_search(start, mid - 1, target)
    elif result[mid] == target:
        return mid
    else:
        return binary_search(mid + 1, end, target)
    
result = [n_list[0]]

for i in range(1, len(n_list)):
    if result[-1] < n_list[i]:
        result.append(n_list[i])
    else:
        result[binary_search(0, len(result) - 1, n_list[i])] = n_list[i]

print(len(result))