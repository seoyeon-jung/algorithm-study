# 나이, 이름 순서대로 입력
# 회원 나이순, 같으면 먼저 가입한 사람 순으로 정렬

N = int(input()) # 회원 수
members = []

for i in range(N):
    age, name = map(str, input().split()) # 나이, 이름 순서
    age = int(age) # int로 변환
    members.append((age, name))

members.sort(key = lambda x : x[0]) # age만 비교

for member in members:
    print(member[0], member[1])