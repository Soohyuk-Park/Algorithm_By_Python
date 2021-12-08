#https://www.acmicpc.net/problem/1062#
# 이런식으로 풀어야 된다는 아이디어는 비슷했는데
# 확실히 구현하는게 어렵기는하다.
# 항상 자기객관화 철저하게 하고. 다시 풀어보고서 잘 안풀리면 다시 복습하고
# 어렵다 어려워~ ㅠㅜ

from itertools import combinations
n, k = map(int, input().split())
if k < 5:
    print(0)
else:
    k -= 5
    nece_chars = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    alpha = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars))}
    cnt = 0
    for _ in range(n):
        tmp = 0
        for c in set(input())-nece_chars:# 여기 For ansdptj tmp =0 에서 ==> 포함한 문자 부분들이 다 1로 바뀐다.
            tmp |= (1 << alpha[c]) # tmp와 (1 << alpha[c])의 Or연산 후에 그걸 tmp에 반환
        input_chars.append(tmp) # 1001001100 같은 식으로 input_chars에는 우리가 받은 단어들의 알파벳 들이 2진수로 들어가있다.
    power_by_2 = (2**i for i in range(21))
    for comb in combinations(power_by_2, k):
        test = sum(comb) # 1001001101 처럼 1이 5개 있는것들이 Test인데. 쭉쭉 모든 1이 5개 있는 test를 진행한다.

        ct = 0
        for cb in input_chars:
            if test & cb == cb:# test와 비교해서 and연산을 했는데 그대로면 포함되는 문자다! 즉 ct에 +1을 해준다.
                ct += 1

        cnt = max(cnt, ct)
    print(cnt)
    
import sys, itertools, string

def cnt(bit, words):
    res = 0
    for i in words:
        if (i & bit) ^ i == 0:
            res += 1
    return res


#  peisea0830 님의 풀이 ( in 백준 )
# n, k = map(int, sys.stdin.readline().split())
# arr = []
# for _ in range(n):
#     arr.append(sys.stdin.readline().rstrip())
# if k < 5:
#     print(0)
# else:
#     bit = []
#     for i in arr:
#         temp = 0
#         for j in i:
#             temp |= (1 << (ord(j) - ord('a')))
#         bit.append(temp)
#     total = []
#     base = ['a', 'n', 't', 'i', 'c']
#     for i in string.ascii_lowercase:
#         if i in base:
#             continue
#         total.append(ord(i) - ord('a'))
#     now = 0
#     for i in base:
#         now |= (1 << (ord(i) - ord('a')))
#     ans = cnt(now, bit)
#     for i in itertools.combinations(total, k - 5):
#         temp = now
#         for j in i:
#             temp |= (1 << j)
#         ans = max(ans, cnt(temp, bit))
#     print(ans)
