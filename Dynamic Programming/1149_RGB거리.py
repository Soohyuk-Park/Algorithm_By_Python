n = int(input()) #집이 몇개니? 입력 받읍시다~

cost = [] #이거는 각 줄에 비용을입력을 받을 예정입니다.
ans = [] # 여기에다가 비용의 최솟값들을 넣어둬서 나중에 답을 출력하면 되겠지요~

for i in range(n):# 일단 비용 입력 시켜주시구여
   cost.append(list(map(int, input().split())))

ans.append((cost[0]))# ans는 그 집까지 했을때. 최솟값들을 담아둔건데. 그니까는
#마지막에 00색으로 칠했을때 비용의 최소가 여기에 담긴다.
#근데 ans[n-1][ 0,1,2 ]중에 하나 들어가는데 0이면 R, 1이면 G, 2이면 B뭐 요런식의 느낌~

for i in range(1, n):
   pre = ans[-1] #이거는 항상 그 전의 정답을 저장합시다.
   A = (cost[i][0] + min(pre[1],pre[2]))
   B = (cost[i][1] + min(pre[0],pre[2]))#A,B,C부분은 i번째 행 까지 왔을때 최솟값들을 갱신
   C = (cost[i][2] + min(pre[1],pre[0]))
   ans.append([A,B,C])#ans라는 리스트의 i번째에는 원소 3개짜리 리스트가 있는데 각 엘리먼트는 거기까지의 최솟값 포함

print( min(ans[n-1]))