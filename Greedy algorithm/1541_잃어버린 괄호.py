# https://www.acmicpc.net/problem/1541

L = input().split('-')
answer = []
for i in L:
    tmp = 0
    A = i.split('+')
    for j in A:
        tmp += int(j)
    answer.append(tmp)
AA = answer[0]
for i in range(1,len(answer)):
    AA -= answer[i]
print(AA)