# https://www.acmicpc.net/problem/2470

n = int(input())
L = list(map(int,input().split()))
L.sort()
left = 0
right = n-1
diff = int(1e10)
answer =[]
while left<right:
    LL = L[left]
    RR = L[right]
    total = LL + RR
    if( abs(total) < diff):
        diff = abs(total)
        answer = [LL,RR]
    if( total < 0):
        left += 1
    else:
        right -=1
print(answer[0],answer[1])