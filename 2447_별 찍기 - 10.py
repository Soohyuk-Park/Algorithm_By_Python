#https://www.acmicpc.net/problem/2447

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def append_star(LEN):
    if LEN==1:
        return['*']
    Stars = append_star(LEN//3)
    L = []
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L
n = int(input())
print('\n'.join(append_star(n)))