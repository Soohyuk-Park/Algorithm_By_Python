# https://www.acmicpc.net/problem/1874
# 자료 구조
# 스택
from collections import deque
c = 0
N = int(input())
answer = []
arr = []
for i in range(N):
    k = int(input())
    answer.append(k)

outt = deque()
for i in range(1,N+1):
    outt.append('+')
    arr.append(i)
    while 1:
      if(arr[-1] == answer[c]):
          arr.pop()
          outt.append('-')
          c += 1
          if c == N or not arr:
              break
      else:
          break

if( len(outt) == 2*N):
    for i in range(len(outt)):
        print(outt.popleft())
else:
    print("NO")
