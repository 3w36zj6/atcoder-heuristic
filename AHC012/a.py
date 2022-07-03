N, K = map(int, input().split())
(*a,) = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(N)]

cut_count = 0
cut_positions = []

import math

d = 1
for i in range(10):
    cut_count += 2
    cut_positions.append(
        [
            10000 * math.cos(math.radians(d)) - 7000,
            10000 * math.sin(math.radians(d)) - 3000,
            10000 * math.cos(math.radians(d + 180)) - 7000,
            10000 * math.sin(math.radians(d + 180)) - 3000,
        ]
    )
    cut_positions.append(
        [
            10000 * math.cos(math.radians(-d)) - 7000,
            10000 * math.sin(math.radians(-d)) - 3000,
            10000 * math.cos(math.radians(-d + 180)) - 7000,
            10000 * math.sin(math.radians(-d + 180)) - 3000,
        ]
    )
    d += 1.05 * i + 1


d = 150
for i in range(18):
    cut_count += 1
    cut_positions.append(
        [
            d - 4000,
            10000,
            d - 4000,
            -10000,
        ]
    )
    if i < 9:
        d += 60 * i + 480
    else:
        d += 900


d = 10
for i in range(10):
    cut_count += 1
    cut_positions.append(
        [
            10000 * math.cos(math.radians(d)) - 7000,
            10000 * math.sin(math.radians(d)) + 7000,
            10000 * math.cos(math.radians(d + 180)) - 7000,
            10000 * math.sin(math.radians(d + 180)) + 7000,
        ]
    )
    d -= 0.9 * i + 1

d = 0
for i in range(10):
    cut_count += 1
    cut_positions.append(
        [
            10000 * math.cos(math.radians(d)) - 7000,
            10000 * math.sin(math.radians(d)) + 4000,
            10000 * math.cos(math.radians(d + 180)) - 7000,
            10000 * math.sin(math.radians(d + 180)) + 4000,
        ]
    )
    d -= 0.9 * i + 1

d_init = -130
d = 0.4
for i in range(5):
    cut_count += 2
    cut_positions.append(
        [
            10000 * math.cos(math.radians(d_init + d)) - 0,
            10000 * math.sin(math.radians(d_init + d)) + 10000,
            10000 * math.cos(math.radians(d_init + d + 180)) - 0,
            10000 * math.sin(math.radians(d_init + d + 180)) + 10000,
        ]
    )
    cut_positions.append(
        [
            10000 * math.cos(math.radians(d_init - d)) - 0,
            10000 * math.sin(math.radians(d_init - d)) + 10000,
            10000 * math.cos(math.radians(d_init - d + 180)) - 0,
            10000 * math.sin(math.radians(d_init - d + 180)) + 10000,
        ]
    )
    d += 1.1 * i + 1


d = 10
for i in range(10):
    cut_count += 1
    cut_positions.append(
        [
            -d - 4500,
            10000,
            -d - 4500,
            -10000,
        ]
    )
    d += 75 * i + 200

cut_count += 4
cut_positions.append(
    [
        -10000,
        -9000,
        10000,
        -9000,
    ]
)
cut_positions.append(
    [
        -10000,
        -8000,
        10000,
        -8000,
    ]
)
cut_positions.append(
    [
        -10000,
        -6800,
        10000,
        -6800,
    ]
)
cut_positions.append(
    [
        -10000,
        -5700,
        10000,
        -5700,
    ]
)


print(cut_count)
for cut_position in cut_positions:
    print(*map(int, cut_position))
