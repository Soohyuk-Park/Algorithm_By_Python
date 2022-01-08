import sys
input = sys.stdin.readline
n, necess = map(int,input().split())
L = list(map(int,input().split()))
end = max(L)
start = 0
tmp = -( sys.maxsize )
while start<=end:
    answer = 0
    mid = (end + start) // 2
    for i in range(len(L)):
        if(L[i] <= mid):
            continue
        else:
            answer += L[i] - mid
    if( answer >= necess):
       tmp = max( tmp , mid)
       start = mid + 1
    else:
       end = mid-1
print(tmp)