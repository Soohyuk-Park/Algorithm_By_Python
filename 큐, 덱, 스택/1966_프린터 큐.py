# https://www.acmicpc.net/problem/1966

from collections import deque
T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    importance = deque(map(int,input().split()))
    impor = deque()
    answer = deque()
    for i in range(n):
        impor.append((i,importance.popleft()))

    while impor:
      K = 1
      while K:
           for i in range(1,len(impor)):
              if(impor[0][1] < impor[i][1]):
                  X = impor.popleft()
                  impor.append(X)
                  K = 1
                  break
              elif(i == len(impor) - 1):
                  K = 0
           if(len(impor) == 1):
               K = 0
      answer.append(impor.popleft())
    for i in range(len(answer)):
        if(answer[i][0] == m):
            print(i+1)
            break



# 다른분의 풀이
# From " https://assaeunji.github.io/python/2020-05-04-bj1966/ "

test_cases = int(input())

for _ in range(test_cases):
    n, m = list(map(int, input().split()))
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0

    while True:
        # 첫번째 if: imp의 첫번째 값 = 최댓값?
        if imp[0] == max(imp):
            order += 1

            # 두번째 if: idx의 첫 번째 값 = "target"?
            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))