# https://www.acmicpc.net/problem/1041 #

import sys

dice = []

n = int(input())

dice = list(map(int, input().split())) #주사위에 써질 눈의 크기를 입력합니다.

#제가 접근한 방법은 이렇습니다.
#주사위를 이어붙이면 밖에서 봤을때 1면만 보이는 주사위 2면,3면만 보이는 주사위로 나눠집니다.
#물론 1개의 주사위인 경우에는 예외적으로 5면이 보이지만 그 경우는 예외처리하면 되겠죠
#그래서 저는 각 경우에 1면 2면 3면에서 나올 수 있는 최소값을 one, two, thr로 설정하기로 했습니다.

answer = 0
one = min(dice)
two = dice[0] + dice[1]
thr = dice[0] + dice[1] + dice[2]

for i in range(6):
   for j in range(6):
      if(i+j != 5 and i != j):
         two = min(two, dice[i]+dice[j])
    #여기에서 두개를 더해서 5가되면 안되고 && 두개가 같으면 안된다고 인덱스에 대한 제약을 주었습니다.
    #달라야 하는건 당연한데, 더해서 5되는건 왜 그럴까요? 맞습니다. 마주보면 드러나는 2면으로 선택할 수 없죠.

for i in [0, 5]:
    for j in [1, 4]:
        for k in [2, 3]:
           thr = min(thr, dice[i] + dice[j] + dice[k])
            #3면 주사위는 이런식으로 마주보는 것들 각각에서 1개씩 고르는 느낌으로~


if(n==1): # 아까 말했던 주사위 하나인 경우의 예외처리. 그냥 5면 보이니까 제일 작은것만 빼주세용
      answer = sum(dice) - max(dice)

elif(n >= 2): # 이거는 그냥 계산 좀 해서 식 구했어요. 뭔가 프로그래밍적인 느낌은 아니고 수학문제 푸는 느낌인데
    #프로그래밍적인 센스를 활용한다면 그냥 식 쓰는게 아니라 다른 방법이 있으려나요?? 흠 일단은 이렇게 마무리
   answer = one*( (n**2 - 3*n + 2)*4 + (n-2)**2) + two *( 4*(2*n - 3)) + thr*(4)

print(answer)
