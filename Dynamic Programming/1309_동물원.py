# https://www.acmicpc.net/problem/1309
# 처음에 다 됐는데, 1을 넣었을때 3이 나오는걸 체크 못했다. 왠지 마지막에 계속 틀렸다고 하더라


import sys
input = sys.stdin.readline

n = int(input().rstrip())

empty = 1
L = 1
R = 1


for i in range(1,n+1):
    if( n == 1):
        print(3)
        break
    empty,L,R =(empty + L + R),empty+R,empty+L
    if( i == n-1 ):
        answer = empty + L + R
        print(answer % 9901 )
        break