# https://www.acmicpc.net/problem/10814
n = int(input())
list = []

for i in range(n):
    key, value = map(str,input().split())
    key = int(key)
    list.append((key,value))

list.sort(key= lambda x : x[0])
for one in list:
    print(one[0], one[1])