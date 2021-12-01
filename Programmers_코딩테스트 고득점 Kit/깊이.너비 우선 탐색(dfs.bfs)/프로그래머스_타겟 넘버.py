# https://programmers.co.kr/learn/courses/30/lessons/43165 #

def solution(numbers, target):
  answer = 0
  n = len(numbers)
  R = [0] * len(numbers)
  for i in range(len(numbers)):
    R[i] = -numbers[i]
  T = [numbers, R]

  for i in range(2 ** (n) - 1):
    A = list((bin(i))[2:])
    for j in range(len(A)):
      A[j] = int(A[j])
    soo = [0] * (n - len(A))
    soo += A
    # print(soo)
    # print((T[soo[0]][0] + T[soo[1]][1] + T[soo[2]][2] + T[soo[3]][3] + T[soo[4]][4]))\
    Totarget = 0
    for i in range(n):
        Totarget += T[soo[i]][i]
    if( Totarget == target):
        answer += 1
  return answer

#훨씬 좋은 풀이인듯. 생각하기는 좀 어렵지만 익숙해지면 활용 가능할 정도. 자신감! 복습! 연습!
"""def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])"""
