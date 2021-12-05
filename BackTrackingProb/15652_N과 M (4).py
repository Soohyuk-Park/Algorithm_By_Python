## https://www.acmicpc.net/problem/15652 ##

n,m = map(int,input().split())

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(1, n+1):
        if s == []:
            s.append(i)
        elif s[-1] <= i:
            s.append(i)
        else:
            continue
        dfs()
        s.pop()


dfs()