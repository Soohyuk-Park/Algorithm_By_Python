# https://www.acmicpc.net/problem/11054 #

#전반적인 아이디어를 서술해보자면
#일단 수열이 있을거니까 그거에 대해서 증가하는 수열중 가장 길이가 긴것을 구해준다.
#그리고 수열을 뒤집는다. 순서만 거꾸로.( 즉 마지막 인덱스가 처음으로 오고. 그런식으로 쭉쭉)
#그리고 거꾸로도 위에랑 똑같이 증가하는 가장 긴 수열을 구한다.
#이제는 두개를 더하고 1을 빼줘야하는데. 이거는 중간에 있는 인덱스를 두 번 세니까 그렇다( 수열의 개수 출력이니까 )

n = int(input())

arr = []
arr2 = [0] * n

arr = list(map(int, input().split())) #여기에 입력해주시고
rst1 = [1]
rst2 = [1] * n

for i in range(n):
   arr2[i] = (arr[n-i-1])

for i in range(1, n):
   rst1.append(1)
   for j in range(i):
      if( arr[j] < arr[i]):
        rst1[i] = max(rst1[j]+1, rst1[i])



for i in range(1, n):
   rst1.append(1)
   for j in range(i):
      if (arr2[j] < arr2[i]):
         rst2[i] = max(rst2[j] + 1, rst2[i])

rst3 = [0] * n
for i in range(n):
   rst3[i] = rst1[i] + rst2[n-i-1]

print(max(rst3)-1)
