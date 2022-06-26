from collections import deque
total, now, goal, up, down = map(int,input().split())

L = [0]*(total+1)
visited = [False]*(total+1)
visited[now] = True
d = deque()
d.append(now)
while d:
    now_pos = d.popleft()
    visited[now_pos] = True
    for i in (up,-down):
        new_pos = now_pos + i
        if 0 < new_pos < total+1:
            if not visited[new_pos]:
                L[new_pos] = L[now_pos] + 1
                visited[new_pos] = True
                if new_pos == goal:
                    print(L[new_pos])
                    exit(0)
                d.append(new_pos)

print('use the stairs')