# https://www.acmicpc.net/problem/4949
# 자료 구조
# 문자열
# 스택
while 1:
    word = input()
    if word=='.':
        break

    L = []
    check = 1
    for i in word:
        if i == '(':
            L.append(0)
        elif i == '[':
            L.append(1)
        elif i == ')':
            if len(L) == 0:
                check =0
                break
            elif L.pop() != 0:
                check = 0
                break
        elif i == ']':
            if len(L) == 0:
                check = 0
                break
            elif L.pop() != 1:
                check = 0
                break
    if len(L) == 0 and check:
        print("yes")
    else:
        print("no")