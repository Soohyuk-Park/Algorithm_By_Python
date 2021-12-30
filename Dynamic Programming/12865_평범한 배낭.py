# https://www.acmicpc.net/problem/12865

N, max_weigh = map(int,input().split())
table = [0] * ( max_weigh + 1)
for _ in range(N):
    weigh, value = map(int,input().split())
    if max_weigh < weigh:
        continue
    else:
       for j in range(max_weigh,0,-1):
           if(j+weigh <= max_weigh and table[j] != 0):
               table[j + weigh] = max(table[j+weigh], table[j] + value)
       table[weigh] = max(table[weigh], value)

print(max(table))