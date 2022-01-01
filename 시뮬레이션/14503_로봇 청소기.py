# https://www.acmicpc.net/problem/14503

r,c = map(int,input().split())
state = list(map(int,input().split()))

D = [(-1,0),(0,1),(1,0),(0,-1)]
mapping = []
for i in range(r):
    L = list(map(int,input().split()))
    mapping.append(L)
Q = len(mapping[0])
visited =[[False]* Q for _ in range(r)]
total = 0
check = 1
while check:
    cnt = 0
    x,y = state[0],state[1]
    visited[x][y] = True
    for i in range(4):
        dir = ( state[2] + 3 * (i + 1) ) % 4
        dx, dy = D[dir][0], D[dir][1]
        x_n, y_n = x+dx , y+dy
        if( mapping[x_n][y_n] == 0 and visited[x_n][y_n] == False ):
           total += 1
           state = [x_n,y_n,dir]
           break
        else:
          cnt+=1
          if(cnt == 4):
              dx, dy = D[dir][0], D[dir][1]
              x_n, y_n = x - dx, y - dy
              if(mapping[x_n][y_n] != 1):
                  state = [x_n,y_n,dir]
              else:
                  check = 0


print(total+1)