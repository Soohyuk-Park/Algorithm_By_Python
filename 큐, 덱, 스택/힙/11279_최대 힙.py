# https://www.acmicpc.net/problem/11279

import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
arr = []

for _ in range(n):
    k = int(input())
    arr.append(k)

for i in range(len(arr)):
    n = arr[i]
    if( n != 0):
        heapq.heappush(q,(-n,n))
    else:
        if(not q):
            print(0)
        else:
            x,y = (heapq.heappop(q))
            print(y)
