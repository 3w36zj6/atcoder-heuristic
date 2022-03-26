from decimal import Decimal

from heapq import heappop, heappush

def dijkstra(graph, start):
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents

S_I, S_J, T_I, T_J, P = input().split()
S_I, S_J, T_I, T_J = map(int,(S_I, S_J, T_I, T_J))
P = Decimal(P)
H = [list(map(int,list(input()))) for _ in range(20)]
V = [list(map(int,list(input()))) for _ in range(19)]

graph = [[] for _ in range(20*20)]

# 横の壁チェック
for i in range(20):
    for j in range(19):

        if not H[i][j]:

            graph[20*i+j].append([20*i+j+1, 1])
            graph[20*i+j+1].append([20*i+j, 1])

# 縦の壁チェック
for i in range(19):
    for j in range(20):
        pass
        if not V[i][j]:
            graph[20*i+j].append([20*(i+1)+j, 1])
            graph[20*(i+1)+j].append([20*i+j, 1])

#print(graph)

dist, parents = dijkstra(graph, 20*S_I+S_J)

directions = [20*T_I+T_J]
while directions[-1] != 20*S_I+S_J:
    p = parents[directions[-1]]
    directions.append(p)

#print(dist[20*T_I+T_J], directions)
directions_ij = [(d//20, d%20) for d in directions[::-1]]


answer = ""

takahashi_position = [S_I, S_J]

for turn in range(200):
    pass
    #input()
    answer += "D" if turn % 2 == 0 else "U"

print(answer)



print(H)