# https://www.acmicpc.net/problem/1003 #
#나중에 더 효율적인 방식을 고려해볼것
ans = []
n= int(input())

ans.append([1,0])
ans.append([0,1])
ans.append([1,1]) #처음 몇개에 대해서 만들어두고, 하나씩 추가하는 식으로 다이나믹 프로그래밍

for i in range(3, 41):
   pre = ( ans[i-1][0] + ans[i-2][0] , ans[i-1][1] + ans[i-2][1] )
   ans.append(pre)



for i in range(n):
   k = int(input())
   for j in range(2):#이쪽 부분에선 그냥 출력
      print(ans[k][j], end =' ')
   print('')
