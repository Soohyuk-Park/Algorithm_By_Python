# https://www.acmicpc.net/problem/4963

while 1:
    c, r = map(int,input().split())
    if( r==0 and c == 0):
        break
    L = []
    tmp = 0
    visited = [[False] * c for _ in range(r)]
    for i in range(r):
        L.append(list(map(int,input().split())))
    D = [[0,1,-1],[0,1,-1]]
    def dfs(a,b):
        if( L[a][b] == 1 and visited[a][b] == False):
            visited[a][b] = True
        for x in D[0]:
          for y in D[1]:
           if( x != 0 or y != 0):
               a_n = a + x
               b_n = b + y
               if(0<=a_n<r and 0<=b_n<c and visited[a_n][b_n] == False and L[a_n][b_n] == 1):
                   visited[a_n][b_n] = True
                   dfs(a_n,b_n)
    for i in range(r):
        for j in range(c):
            if(visited[i][j] == False and L[i][j] == 1):
                dfs(i,j)
                tmp+=1
    print(tmp)
