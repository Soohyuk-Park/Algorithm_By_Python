# https://www.acmicpc.net/problem/2110

n,m = map(int,input().split())

arr = []
for i in range(n):
    k = int(input())
    arr.append(k)
arr.sort()
start = 1
end = arr[-1] - arr[0]
answer = 0
while( start <= end ):
    mid = ( start + end )//2
    count = 1
    current = arr[0]
    for i in range(1,len(arr)):
        if(arr[i] >= current + mid ):
            current = arr[i]
            count += 1
    if( count >= m):
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)