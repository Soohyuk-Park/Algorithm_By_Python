# https://programmers.co.kr/learn/courses/30/lessons/42860 #

def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [ i for i in range(14) ] + [ j for j in range(12,0,-1)]
        return num_char[ord(char)- ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)
    move = n - 1
    for idx in range(n):
        next_idx = idx+1
        while(next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        forwardMoving = idx
        backMoving = n - next_idx
        distance = min( forwardMoving, backMoving )
        move = min( move ,  forwardMoving + backMoving + distance )
    answer += move
    return answer
        # distance를 정의함으로써 뒤로 갔다가 앞으로 가는게 더 효율적일 수 있다는 사실을 시사한다.
#이러한함수는 해당 문자열까지 도달하려면 몇번 위, 아래 방향키를 눌러야 하는지에 대한 정보를 보여준다.
#num_char : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

if __name__ == '__main__':
    print(solution("ABDDD"))

