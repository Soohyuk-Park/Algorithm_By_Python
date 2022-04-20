import sys
from collections import Counter
from collections import defaultdict as dd
input = sys.stdin.readline

# First Function
def ecology():
    tree_list = []
    while 1:
        tree_name = input().rstrip()
        if not tree_name:
            break
        tree_list.append(tree_name)
    tree_list.sort()
    tree_counter = Counter(tree_list)
    cardinalityOfTree = 0
    for key in tree_counter:
        cardinalityOfTree += tree_counter[key]
    answer = []
    for name in tree_counter:
        # tree_percent = round(tree_counter[name] * 100 / cardinalityOfTree, 4 )
        tree_percent = f"{((tree_counter[name] / cardinalityOfTree) * 100):.4f}"
        answer.append((name, tree_percent))
    answer.sort(key=lambda x: x[0])
    for now in answer:
        print(now[0],end=" ")
        print(now[1])
    return 0

#Second Function
def ecology2():
    d = dd(int)
    n = 0
    while True:
        s=input().rstrip()
        if not s:
            break
        d[s] += 1
        n += 1
    for key in sorted(d.keys()):
        r = d[key] / n * 100
        r = '{:.4f}'.format(r)
        print(f'{key} {r}')



if __name__ == "__main__":
    #ecology()
    ecology2()






