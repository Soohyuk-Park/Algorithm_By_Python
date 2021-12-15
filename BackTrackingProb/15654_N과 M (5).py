# https://www.acmicpc.net/problem/15654
# 이번엔 combinations가 아니라 permutaions를 이용하는 문제
# 리스트로 옮기는데 좀 헷갈려서 몇 번 틀리다가 맞췄다.

from itertools import permutations

n, m = map(int, input().split())

arr = list(map(int,input().split()))

arr.sort()
l = []

for a in permutations(arr, m):
    a = list(a)
    l.append(a)


for i in range(len(l)):
    for j in range(m):
        if( j != m-1):
           print(l[i][j],end=' ')
        else:
           print(l[i][j])



## 궁금한 코드
from itertools import*;n,m=map(int,input().split())
for x in permutations(sorted(map(int,input().split())),m):print(*x)
## 프린트에 왜 *가 붙어있는거지???????? 띄어쓰기인가?
import sys
from itertools import permutations
ssr = sys.stdin.readline

N, M = list(map(int, ssr().split()))
arr = list(map(int, ssr().split()))

arr = list(permutations(arr, M))
arr.sort()
for i in arr:
    print(*i)## 리스트에 있는거 한칸씩 띄워서 출력하는 것 같기는한데 구글링이 안되넹