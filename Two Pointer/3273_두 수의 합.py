# https://www.acmicpc.net/problem/3273 #

import sys

if __name__ == '__main__':
    N = int(input()) #숫자 개수 입력 받고
    arr = list(map(int, sys.stdin.readline().split()))
    X = int(input()) #목표하는 값
    arr.sort() #일단 배열은 오름차순으로 설정해주시고
    left, right = 0, N - 1 #left , right가 처음과 끝을 나타낸다!
    ans = 0 # 만족하는 쌍이 몇개인지 봐야되니까 처음엔 0개고, 맞을때마다 하나씩 플러스~

    while left < right: # 당연한 조건. 만족안되면 바로 종료!
        tmp = arr[left] + arr[right]#왼쪽에 있는 어떤수와 우측의 수를 합해서 tmp라고 하자.
        if tmp == X: ans += 1 # 목표값이면 정답에 1 추가
        if tmp < X: # 작으면 일단 왼쪽부터 하나씩 늘려
            left += 1
            continue
        right -= 1 #왼쪽을 늘렸더니 너무 커졌으면 우측에서는 좀 줄이자.
    print(ans)
