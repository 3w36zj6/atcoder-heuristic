N, T = map(int, input().split())
tiles = [list(map(lambda x: int(x, 16), input())) for _ in range(N)]

# print(tiles)

import random

ans = ""

for i in range(N):
    for j in range(N):
        if tiles[i][j] == 0:
            start_i, start_j = i, j

if start_i <= T:
    ans += "U" * start_i
    T -= start_i

if start_j <= T:
    ans += "L" * start_j
    T -= start_j

# print(ans, T//4)

l = []
cycle = 4 * (N - 1)
# print(T, cycle)
while T > cycle:
    tmp = []
    tmp.extend(["R" for _ in range(cycle // 4)])
    tmp.extend(["D" for _ in range(cycle // 4)])
    l.extend(random.sample(tmp, len(tmp)))
    tmp = []
    tmp.extend(["L" for _ in range(cycle // 4)])
    tmp.extend(["U" for _ in range(cycle // 4)])
    l.extend(random.sample(tmp, len(tmp)))
    T -= cycle

print(ans + "".join(l))
