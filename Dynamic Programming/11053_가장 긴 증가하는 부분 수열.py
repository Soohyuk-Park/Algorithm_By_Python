n = int(input())

arr = []
chk = [] #check리스트에는 그 인덱스까지 증가하는 최대 개수가 몇개인지 기록한다.

arr = list(map(int, input().split())) #여기에 입력해주시고

chk.append(1) #처음엔 당연히 증가하는 개수가 1개겠지요

for i in range(1, n):
   chk.append(1)
   for j in range(i):
       if( arr[j] < arr[i] ): # 이부분이 핵심. 더 크면 그 전까지의 증가순열 개수에 더해준다.
           chk[i] = max( chk[j] + 1, chk[i])# 그거중에서도 제일 큰거를 골라야지

print(max(chk))