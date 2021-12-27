# https://www.acmicpc.net/problem/2166

n = int(input())
arr = []
ans1 = 0
ans2 = 0
for i in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
arr.append(arr[0])

for i in range(n):
    ans1 += arr[i][0] * arr[i+1][1]
    ans2 += arr[i][1] * arr[i+1][0]
print(abs(ans1-ans2) / 2)