# https://programmers.co.kr/learn/courses/30/lessons/42748 #
# 2번째 풀이도 잘 알아두자. 아직은 lambda의 활용에 있어서 익숙하지 않고, 실전적인 활용에 한계가 많다.

def solution(array, commands):
    answer = []
    for i,j,k in (commands):
        arr1 = []
        arr1 = array[i-1:j]
        answer.append(arr1[k-1])
    return answer

solution([1,2,3,4,5],[[2,4,1]])


# lambda함수를 이용한 좋은 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
