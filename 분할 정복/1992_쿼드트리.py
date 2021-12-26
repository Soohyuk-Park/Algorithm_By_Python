import sys
input = sys.stdin.readline

N = int(input())
L = [list(map(int,input().strip())) for _ in range(N)]
def paper_cut(x,y,n):
    check = L[x][y]
    for i in range(n):
        for j in range(n):
            if(L[x+i][y+j] != check):
                print('(', end='')
                paper_cut(x,y,n//2)
                paper_cut(x, y+n//2, n // 2)
                paper_cut(x+n//2, y, n // 2)
                paper_cut(x+n//2, y+n//2, n // 2)
                print(')',end='')
                return
    if check == 0:
        print(0,end='')
        return
    else:
        print(1,end='')
        return

paper_cut(0,0,N)