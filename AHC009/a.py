from decimal import Decimal

import random

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


def search_directions(s_i, s_j):
    dist, parents = dijkstra(graph, 20*s_i+s_j)

    directions = [20*T_I+T_J]
    while directions[-1] != 20*s_i+s_j:
        p = parents[directions[-1]]
        directions.append(p)

    directions_ij = [(d//20, d%20) for d in directions]

    return directions_ij

directions_ij = search_directions(S_I, S_J)

mid_ij = directions_ij[len(directions_ij)//2]

answer = []

takahashi_position = [S_I, S_J]

for turn in range(200):
    answer.append(random.choice("UDDLRR"))
    #print(turn, len(directions_ij))
    if len(directions_ij) <= 1:
        directions_ij = search_directions(*mid_ij)
        mid_ij = directions_ij[len(directions_ij)//2]
    else:
        pass
        if directions_ij[-1][0] != directions_ij[-2][0]:#縦移動
            answer[-1] = "D" if directions_ij[-2][0] - directions_ij[-1][0] > 0 else "U"
        elif directions_ij[-1][1] != directions_ij[-2][1]:#横移動
            answer[-1] = "R" if directions_ij[-2][1] - directions_ij[-1][1] > 0 else "L"

        directions_ij.pop()


print("".join(answer))
