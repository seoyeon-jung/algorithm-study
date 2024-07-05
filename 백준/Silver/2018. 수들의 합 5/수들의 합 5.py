N = int(input())

count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != N:
    if sum == N: #입력한 전체 합한 수
        count += 1
        end_index += 1
        sum += end_index
    elif sum > N:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)