# https://www.acmicpc.net/problem/9375

from collections import Counter
test_case = int(input())
for i in range(test_case):
    num_of_things = int(input())
    my_bag = []
    for j in range(num_of_things):
        a,b = input().split()
        my_bag.append(b)
    num = 1
    bag_counter = Counter(my_bag)
    for key in bag_counter:
        num *= bag_counter[key] + 1
    print(num-1)





