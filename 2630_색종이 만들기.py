# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

N = int(input())
L = [list(map(int,input().split())) for _ in range(N)]
white = 0
blue = 0

def paper_cut(x,y,n):
    global white, blue
    check = L[x][y]
    for i in range(n):
        for j in range(n):
            if(L[x+i][y+j] != check):
                paper_cut(x,y,n//2)
                paper_cut(x, y+n//2, n // 2)
                paper_cut(x+n//2, y, n // 2)
                paper_cut(x+n//2, y+n//2, n // 2)
                return
    if check == 0:
        white +=1
        return
    else:
        blue +=1
        return

paper_cut(0,0,N)
print(white)
print(blue)