# https://www.acmicpc.net/problem/2164
# 쏘 이지( 사실 N=1인거 예외 안해서 한 번 틀림.. ㅋㅋ )

from collections import deque

N = int(input())
q = deque()

cnt = 1
if(N == 1):
    cnt =0
    print(1)


for i in range(1,N+1):
   q.append(i)

while cnt:
    q.popleft()
    if( len(q) == 1):
        print(q[0])
        break
    x = q.popleft()
    q.append(x)