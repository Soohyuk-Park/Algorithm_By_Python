#https://www.acmicpc.net/problem/3190
from collections import deque
n = int(input())
apple = deque()
snake = deque()
k=int(input())
D = [(-1,0),(0,1),(1,0),(0,-1)]
time = 0
check = 1
direction = 1
for i in range(k):
    x,y = map(int,input().split())
    apple.append((x-1,y-1))
w = int(input())
dir = deque()
for i in range(w):
    x,y = map(str,input().split())
    x = int(x)
    dir.append((x,y))
snake.append((0,0))
while check:
    if dir:
      if( time == dir[0][0] ):
          if( dir[0][1] == 'D' ):
              direction = ( direction + 1 ) % 4
              trash = dir.popleft()
          else:
              direction = ( direction + 3 ) % 4
              trash = dir.popleft()
    x,y = snake.popleft()
    snake.appendleft((x,y))
    x_n,y_n = x+D[direction][0], y+D[direction][1]
    if( not ( 0<=x_n<n and 0<= y_n<n) ):
        check = 0
    else:
      if( (x_n,y_n) not in snake ):
          snake.appendleft((x_n,y_n))
          if( (x_n,y_n) not in apple ):
              snake.pop()
          else:
              apple.remove((x_n,y_n))
      else:
          check= 0
    time+= 1
print(time)
