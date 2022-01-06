#https://www.acmicpc.net/problem/2467
N = int(input())
L = list(map(int,input().split()))
start = 0
end = N-1
hap = abs(L[start] + L[end])
check = 0
now = (L[start],L[end])
while start < end:
    if( L[start]+L[end] < 0):
       start += 1
       if hap > abs(L[start]+L[end]) and start != end:
          hap = abs(L[start] + L[end])
          now = (L[start],L[end])
    elif(L[start]+L[end] == 0):
       now = (L[start],L[end])
       break
    else:
       end -=1
       if hap > abs(L[start]+L[end]) and start != end:
          hap = abs(L[start]+L[end])
          now = (L[start],L[end])

print(*now)