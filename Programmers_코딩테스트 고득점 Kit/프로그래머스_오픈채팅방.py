# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    for i in range(len(record)):
        record[i] = list(record[i].split(' '))

    dict = {}

    for i in range(len(record)):
        if (record[i][0] == 'Enter'):
            dict[record[i][1]] = record[i][2]
        elif (record[i][0] == 'Change'):
            dict[record[i][1]] = record[i][2]

    answer = []
    for i in range(len(record)):
        if (record[i][0] == 'Enter'):
            answer.append(str(dict[record[i][1]]) + '님이 들어왔습니다.')
        elif (record[i][0] == 'Leave'):
            answer.append(str(dict[record[i][1]]) + '님이 나갔습니다.')

    return answer