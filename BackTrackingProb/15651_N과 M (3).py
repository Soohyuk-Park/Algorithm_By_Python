## https://www.acmicpc.net/problem/15651 ##

n,m = map(int, input().split())

s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(1, n+1):
        s.append(i)## 이 문제는 같은걸 출력해도 상관없으니 그냥 for문으로 계속 더해줍시다.
        dfs()#별다른 제약조건이 없기에 오히려 M과N시리즈중에 제일 쉽다고 느껴지네요.
        s.pop()

dfs()