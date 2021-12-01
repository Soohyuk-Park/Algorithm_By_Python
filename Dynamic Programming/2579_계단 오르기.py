# https://www.acmicpc.net/problem/2579 #

n = int(input())
arr = [0 for _ in range(302)]
score = [0 for _ in range(302)]
for i in range(1, n+1):
    arr[i] = (int(input()))
print(arr)

score[1] = arr[1]
score[2] = arr[2]+arr[1]
score[3] = max(arr[1] + arr[3],arr[2]+arr[3])
for i in range(4, n+1):
    score[i] = max((score[i-3]+arr[i-1]+arr[i]),score[i-2]+arr[i])

print(score[n])