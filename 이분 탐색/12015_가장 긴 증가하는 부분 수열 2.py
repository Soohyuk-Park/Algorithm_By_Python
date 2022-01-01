# https://www.acmicpc.net/problem/12015
import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
lis =[0]

for l in L:
    if lis[-1]< l:
        lis.append(l)
    else:
        left = 0
        right = len(lis)
        while left < right:
            mid = (right + left)//2
            if( lis[mid] < l):
                left = mid +1
            else:
                right = mid
        lis[right] = l
print(len(lis) - 1)