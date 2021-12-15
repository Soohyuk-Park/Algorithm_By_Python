# https://www.acmicpc.net/status?user_id=homeomor997&problem_id=2156&from_mine=1
# 처음에 S[i] = max( S[i-3] + arr[i-1] + arr[i], S[i-2] + arr[i], S[i-1])
# 저거 위에서 S[i-1]을 안넣고 했는데, 넣어줘야한다.
# 비교를 할 때 바로 전에꺼랑의 비교도 필수적으로 해줘야함을 기억하자!

n = int(input())
arr = []

for i in range(n):
   arr.append(int(input()))

S = [0]*len(arr)

S[0] = arr[0]
if len(arr) == 1:
    print(arr[0])
elif(len(arr) == 2):
    print(sum(arr))
else:
 S[1] = arr[0] + arr[1]
 S[2] = max(arr[0] + arr[2],arr[1] + arr[2] ,S[1])
 for i in range(3,len(arr)):
    S[i] = max( S[i-3] + arr[i-1] + arr[i], S[i-2] + arr[i], S[i-1])

 print(max(S))