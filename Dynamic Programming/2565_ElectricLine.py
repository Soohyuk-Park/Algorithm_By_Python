import sys

def lis(arr, n): # 이거는 무슨 함수일까요?
  rst = [1] * n  #일단 1로만 이루어진 배열을 만드는데요.
  for i in range( 1 , n):
    for j in range( i ): # i라는 숫자에 대해서 그것보다 작은 것들은 다 탐색해볼거에요.
      if arr[j] < arr[i]: # 만약에 arr[j] < arr[i]라는건 왼쪽 전깃줄이 정렬된 상태에서 오른쪽 전깃줄도 증가 방향이 되는
                          # 부분들을 구하게 되는건데. 이런걸 찾으면 오름차순으로 수열 만드니까 길이를 저장하는 rst에 +!.
        rst[i] = max(rst[i], rst[j]+1 ) # j까지의 증가순열에 1을 더하는데. 그 전에 했던게 더 크면 굳이 초기화 X라서 max
  return max(rst)

def solve():
  n = int(sys.stdin.readline().rstrip()) ##일단 n을 입력받습니다.
  arr = []
  for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((a,b)) # 좌측 전선의 a와 우측 전선의 b가 연결되어있음을 나타내줍니다.
  arr.sort(key = lambda x: x[0])# 좌측 전선의 번호로 오름차순 정렬 시켜줍시다~
  l = [] #빈 리스트 하나 만들어주시구여
  for a, b in arr:
    l.append(b) # 여기다가는 b에 있는거 하나하나 차례대로 넣어줄거에요.
  print(n - lis(l,n)) #최대길이가 lis(l,n)이었으니까 총 길이 - 최대길이 = 없애야하는 전선수

solve()

