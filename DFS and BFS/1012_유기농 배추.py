import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def check(baechu, r, c):
    if( baechu[r][c] == 1):
        baechu[r][c] = 0
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i, j in D:
            if(0<= r+i < n and 0<= c+j< m and baechu[r+i][c+j] == 1):
                check(baechu, r+i, c+j)
    return 0


def finder(graph):
   for i in range(n):
      for j in range(m):
           if( graph[i][j] == 1):
               return (i,j)

T = int(input())

for i in range(T):
   cnt = 0
   n, m, k = map(int, input().split())
   baechu = [[0]*m for _ in range(n)]
   for _ in range(k):
      a,b = map(int, input().split())
      baechu[a][b] = 1

   for _ in range(2500):
       row, col = finder(baechu)
       check(baechu, row, col)
       cnt += 1
       if( not(finder(baechu))):
           break
   print(cnt)
