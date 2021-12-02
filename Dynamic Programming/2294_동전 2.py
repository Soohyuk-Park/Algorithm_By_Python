# https://www.acmicpc.net/problem/2294 #

n,m = map(int,input().split())     #예를 들어보자. n = 10, m = 100

arr = []
d = [10003] * (m+1) # 이거는 인덱스 0부터 100까지 총 101개 있는 d이다.

for i in range(n):
    arr.append(int(input())) # 여기에는 동전의 값이 들어가는데. 일단 뭐 대충 1,3,5,7.. 홀수 원들이 있다고 생각하자.

d[0] = 0 # d[i]는 i원을 만드는데 필요한 동전의 최소개수이고, 따라사 0에선 0값을 가진다.
for i in range(n):  #일단 i일때, (예를 들어서 4일때를 생각해보자)
    for j in range(arr[i], m+1): #arr[4] = 7 이라고 하면. 7부터 101까지 갈거다 그리고 j = 20정도일때
        if(d[j-arr[i]] != 10003): # d[13] != 10003부터 탐색. 즉 이미 앞 동전들로 만들 수 있어야 탐색 할거임
          d[j] = min(d[j], d[j - arr[i]] + 1)# 이미 있는 d[13]에 7원 동전을 더한거랑. 원래 d[j]에 있던거랑 뭐가 클까

if( d[m] == 10003):
    print(-1)
else:
    print(d[m])