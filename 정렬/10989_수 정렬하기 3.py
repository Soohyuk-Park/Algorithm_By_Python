#https://www.acmicpc.net/problem/10989
# pypy3으로하면 메모리 초과라 python3으로 하니까 잘 된다.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N= int(input())
check_list = [0] * 10001

for i in range(N):
    input_num = int(input())
    check_list[input_num] +=1
for i in range(10001):
    if check_list[i] != 0:
        for _ in range(check_list[i]):
            print(i)
