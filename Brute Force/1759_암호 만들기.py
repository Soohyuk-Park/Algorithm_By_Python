## https://www.acmicpc.net/problem/1759
from itertools import combinations
length, num = map(int,input().split())
L = list(map(ord,input().split()))
L.sort()
moum = ['a','e','i','o','u']
for i in combinations(L,length):
    check = 0
    i = [chr(j) for j in i]
    for q in range(5):
        if(moum[q] in i):
            check+=1
    jaum = len(i)-check
    if check and jaum >=2:
      for k in range(len(i)):
            print(i[k],end='')
      print()
    
##################
from itertools import combinations

L, C = map(int, input().split())
candidate = input().split()

vowel = [x for x in candidate if x in ['a', 'e', 'i', 'o', 'u']]
others = [x for x in candidate if x not in ['a', 'e', 'i', 'o', 'u']]

ans = []
for i in range(1, len(vowel) + 1):
    for a in combinations(vowel, i):
        if L - i >= 2:
            for b in combinations(others, L - i):
                ans.append(sorted(a + b))

ans.sort()
for s in ans:
    print("".join(s))
