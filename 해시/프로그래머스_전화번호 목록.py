## https://programmers.co.kr/learn/courses/30/lessons/42577 ##

# 내가 푼 풀이
# 처음에 for문을 두 번 돌리라 했다. 왜냐면 N개 중에 2개씩 뽑아서 다 확인해야 될 것 같아서
# 근데 숫자가 문자열로 주어졌어도 그냥 정렬시키면, 지금 상황에서는 괜찮다.( 결국 같은 문자열이 있는걸 찾는 느낌이니까

def solution(phone_book):
    answer = True
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                print(answer)
                print(i)
                answer = False
                break
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))


## 이게 해시를 이용한 좋은 풀이라고 한다.
# 이런식의 풀이는 아직 생각하지 못하는 것 같은데, 복습해서 잘 소화해두자 ㅜㅜ
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    print(hash_map)

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number # temp는 처음에 비어있는데 phone_number에 있는 수로 하나씩 채워줄거다.
            if temp in hash_map and temp != phone_number: #Temp를 채우다가 해쉬맵에 있는거랑 같아지는데, 자기 자신이 아니라면
                #그러면 겹치는게 있다는거겠지
                answer = False
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))