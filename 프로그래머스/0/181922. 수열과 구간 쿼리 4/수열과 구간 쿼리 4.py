def solution(arr, queries):
    for x, y, z in queries:
        for i in range(x, y+1):
            if i % z == 0:
                arr[i] += 1
    return arr