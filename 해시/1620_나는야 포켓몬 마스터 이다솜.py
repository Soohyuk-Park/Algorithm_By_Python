import sys
input = sys.stdin.readline

num_of_monster, num_of_question = map(int,input().split())
dictSearchingByName = {}
dictSearchingByNumber = {}
idx = 1
for i in range(num_of_monster):
    name_of_monster = input().rstrip()
    dictSearchingByName[name_of_monster] = idx
    dictSearchingByNumber[idx] = name_of_monster
    idx += 1

for i in range(num_of_question):
    query = input().rstrip()
    if query.isdigit():
        print(dictSearchingByNumber[int(query)])
    else:
        print(dictSearchingByName[query])



