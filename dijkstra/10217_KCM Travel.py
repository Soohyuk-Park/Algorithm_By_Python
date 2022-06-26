import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def main():
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))

    dist = [[INF] * (M + 1) for _ in range(N + 1)]
    dist[1][0] = 0

    que = deque([(0, 0, 1)])  # Time Cost Node

    while que:
        time, cost, node = que.popleft()

        if dist[node][cost] < time:
            continue

        for city, c, t, in graph[node]:
            alt_c = cost + c
            alt_t = time + t

            if alt_c <= M and alt_t < dist[city][alt_c]:
                for i in range(alt_c, M + 1):
                    if alt_t < dist[city][i]:
                        dist[city][i] = alt_t
                    else:
                        break
                que.append((alt_t, alt_c, city))

    sol = dist[N][M]

    print(sol if sol != INF else 'Poor KCM')


for ___ in range(int(input())):
    main()