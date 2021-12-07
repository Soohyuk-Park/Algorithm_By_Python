# # https://programmers.co.kr/learn/courses/30/lessons/60057 ##
# 일단 이 문제는 처음 생각보다 어렵지는 않다
# 괜히 문제에 대해 꼬아서 생각했기에 어렵게 느꼈다
# 문제를 잘 읽자는 말은 과외를 하면서 내 입으로도 많이 했던 말인데, 내가 실천을 못하고 있다 ㅜㅜ
#
# 문자열의 처음부터 반복되는걸 찾는거다. 즉 중간부터 반복되거나 반복이 없다가 생기거나 하는것을 고려하지 않는다
# 예를들어서 abcdbcd라는게 있어도 a2bcd로 바꿀수없다. bcd전에 a가 있으니까
# 하지만 abcabcd는 2abcd로 바꿀 수 있다...
# 즉 range로 그냥 순서대로 훑어주면 된다는 소리다.


def solution(s):
    answer = 1000000
    for i in range(1, len(s) // 2 + 2):
        new = ''
        now = s[:i]
        A = 1

        for j in range(i, len(s) + i, i):
            if (now == s[j:j + i]): ## 똑같은 문자열이 있니? 에서 True라면
                A += 1 # 나중에 그 문자열 앞에 붙일 계수에 1을 더해준다.
            else:
                if (A == 1): # 만약 여기로 넘어왔는데 계수가 1이라면
                    new += now # 우리가 이번 i(슬라이싱의 개수 ) 에서 사용할 new에 그냥 더해준다.
                    now = s[j:j + i] # 그리고 now는 그 다음 문자열을 받게끔 바꿔준다.
                else:
                    new = new + str(A) + now # 넘어왔는데 계수가 1이 아니고 더 크다면
                    # 원래있던 new에다가 now앞에 계수를 붙인채로 더해주면 된다.
                    A = 1 # 더하고 나서 계수는 1로 다시 바꿔주고.
                    now = s[j:j + i]

        answer = min(answer, len(new)) #답은 각 i마다 한 번씩 갱신된다. 제일 작은게 답이니까 Min으로

    return answer