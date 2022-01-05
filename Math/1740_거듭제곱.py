# https://www.acmicpc.net/problem/1740
K = bin(int(input()))[2:]
answer = 0

for i in range(len(K)):
    if int(K[i]) == 1:
        answer += 3**(len(K) -i -1 )
print(answer)