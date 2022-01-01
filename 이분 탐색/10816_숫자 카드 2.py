#https://www.acmicpc.net/problem/10816
# 가장 기본적인 풀이는 이분탐색이고, 여기서는 그 이외의 추가적인 풀이법에 대해서만 적어두었다.
# 바로 밑에 있는 풀이가 index와 sort를 이용해 효율성을 높여서 좋은 것 같다.
# hash 문제들도 잘 풀어보면 좋을듯

n = int(input())
card=list(map(int,input().split()))
card.sort()
m=int(input())
searched =list(map(int,input().split()))
cardinality = [0]*(len(searched))
index = 0
m_dic = {}
for s in sorted(searched):
    cnt = 0
    if s not in m_dic:
        while index < len(card):
            if s == card[index]:
                cnt += 1
                index += 1
            elif s > card[index]:
                index += 1
            else:
                break
        m_dic[s] = cnt
print(card)
print(sorted(searched))
print(' '.join(str(m_dic[s]) for s in searched))

###############################################

from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))

####################################################################

from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(C)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))