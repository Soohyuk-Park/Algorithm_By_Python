# https://www.acmicpc.net/problem/1806

length, total = map(int,input().split())
L = list(map(int,input().split()))

summation = [0] *(length + 1)
for i in range(1, length + 1):
    summation[i] = summation[i-1] + L[i-1]


answer = 1000001
start = 0
end = 1

while start != length:
    if summation[end] - summation[start] >= total:
        if end - start < answer:
            answer = end - start
        start += 1
    else:
        if end != length:
            end+=1
        else:
            start += 1
if answer != 1000001:
    print(answer)
else:
    print(0)
