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