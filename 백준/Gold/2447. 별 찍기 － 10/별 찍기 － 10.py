def solution(n):
  if n == 1:
    return ['*']

  Stars = solution(n//3)
  list = []

  for star in Stars:
    list.append(star*3)
  for star in Stars:
    list.append(star+' '*(n//3)+star)
  for star in Stars:
    list.append(star*3)

  return list

N=int(input())
print('\n'.join(solution(N)))