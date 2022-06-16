def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
        return parent[a]
    return parent[a]

def union(fir,sec):
    fir = find(fir)
    sec = find(sec)
    if fir < sec:
        parent[sec] = fir
    else:
        parent[fir] = sec

a,b,c = map(int,input().split())
parent = list(range(a+1))
path = set(map(int,input().split()))
L = []
for _ in range(b):
    x,y,w = map(int,input().split())
    L.append((w,x,y))
L.sort(key = lambda x : x[0])

total=0

while len(path) != a:
    for info in L:
        wei = info[0]
        start = info[1]
        end = info[2]
        if find(start) == find(end):
            continue
        else:
            if start in path and end in path:
                continue
            elif start in path or end in path:
                path.add(start)
                path.add(end)
                union(start, end)
                total += wei
                break
            else:
                continue
print(total)





