def solution(N, stages):
    answer = []
    dict = {}
    ratio = {}
    Ratio = {}
    n = len(stages)
    for i in range(1, N + 2):
      if( i == N+1):
          break
      freq = 0
      total = 0
      for j in range(n):
          if (stages[j] == i):
               freq += 1
      dict[i] = freq
      for q in range(1, i):
           total += dict[q]
      if( total == n): ##처음 제출할때 이 부분때문에 몇개에 런타임 에러가 생겼다. 이런 상황이면 분모가 0이된다.
          ratio[i] = 0 #분모0같이 자주 발생하는 예외 상황은 항상 미리미리 체크하는 습관
      else:
          ratio[i] = float((freq)/(n-total))
    Ratio = sorted(ratio.items(), key=lambda x: x[1], reverse= True)
    for b in range(N):
        answer.append(Ratio[b][0])
    return answer

print(solution(5,[4,4,4,4,4]))