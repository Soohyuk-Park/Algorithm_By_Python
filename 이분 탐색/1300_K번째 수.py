n = int(input())
k = int(input())
start = 1
end = k
answer = 0
while start <= end:
    mid = ( start + end ) // 2
    cnt = 0
    for i in range(1,n+1):
        cnt+= min(mid//i,n)
    if( cnt < k ):
        start = mid + 1
    else:
        answer = mid
        end = mid - 1
print(answer)
