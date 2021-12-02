## https://www.acmicpc.net/problem/1052 ##

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = 0
while bin(N).count('1') > K:
    plus = 2 ** (bin(N)[::-1].index('1'))
    answer += plus
    N += plus
print(answer)

##단순무식하게 처음으로 해봤는데 range만 봐도 안될거같고 이런 코드는 하지말자 ㅜㅜ
#머리를 쓰자 수혁아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ....................
# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
#
# for i in range(10000001):
#     if(list(bin(N+i)).count('1') <= K):
#         print( i )
#         break
#
# ##
