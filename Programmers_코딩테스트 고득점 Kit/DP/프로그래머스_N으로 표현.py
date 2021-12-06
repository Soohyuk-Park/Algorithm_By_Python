# https://programmers.co.kr/learn/courses/30/lessons/42895 #


# arr이라는 행렬의 칸을 채워주는게 핵심이다
# 일단 처음에 arr이라는 리스트의 첫 번째 칸은 비어있고
# 1번째에는 5가 들어가있다
# 2번째부터가 중요한데
# for i 로 시작하는 부분을 보면
# 처음에 i = 2일 때 j = 1이고
# 둘 다 5를 가지고서 사칙연산을 수행하게 된다
# i =3 이 되면
# 하나는 1번째칸, 다른 하나는 2번째 칸에서 숫자를 골라서 사칙연산후 3번째 칸을 채운다
# 4가되면
# 1,3 // 2,2 // 3,1 과 같은 조합도 사용하게 된다.

def solution(N, number):
    if( N == number):
        return 1
    arr = [[]] + [{int(str(N)*i)} for i in range(1,9)]
    for i in range(2,9):
        for j in range(1, i):
           for A in arr[j]:
               for B in arr[i-j]:
                   arr[i].add(A+B)
                   arr[i].add(A-B)
                   arr[i].add(A*B)
                   if B:
                       arr[i].add(A//B)
        if number in arr[i]:
             return i

    return -1
