import random

T = [list(map(int, [*input()])) for _ in range(30)]

ans = [0 for _ in range(900)]

mini_loops = []

for x in range(30):
    for y in range(30):
        if (
            1 < x < 28
            and 1 < y < 28
            and (T[x][y] == 2 or T[x][y] == 4)
            and (T[x][y + 1] == 1 or T[x][y + 1] == 5)
            and (T[x + 1][y] == 3 or T[x + 1][y] == 5)
            and (T[x + 1][y + 1] == 0 or T[x + 1][y + 1] == 4)
        ):

            mini_loops.append((x, y))

for x, y in mini_loops:
    # 右下
    if (
        T[x + 1][y + 1] == 4
        and not T[x + 2][y + 1] in (6, 7)
        and not T[x + 1][y + 2] in (6, 7)
        and not T[x + 2][y + 2] in (6, 7)
    ):

        ans[30 * (x + 1) + y + 1] = 1

        if T[x + 2][y + 1] == 4:
            ans[30 * (x + 2) + y + 1] = 1
        elif T[x + 2][y + 1] <= 3:
            ans[30 * (x + 2) + y + 1] = 3 - T[x + 2][y + 1]

        if T[x + 1][y + 2] == 4:
            ans[30 * (x + 1) + y + 2] = 1
        elif T[x + 1][y + 2] <= 3:
            ans[30 * (x + 1) + y + 2] = (3 - T[x + 1][y + 2] + 2) % 4

        if T[x + 2][y + 2] == 5:
            ans[30 * (x + 2) + y + 2] = 1
        elif T[x + 2][y + 2] <= 3:
            ans[30 * (x + 2) + y + 2] = (3 - T[x + 2][y + 2] + 1) % 4

    # 右上
    if (
        T[x][y + 1] == 5
        and not T[x - 1][y + 1] in (6, 7)
        and not T[x][y + 2] in (6, 7)
        and not T[x - 1][y + 2] in (6, 7)
    ):

        ans[30 * (x) + y + 1] = 1

        if T[x - 1][y + 1] == 5:
            ans[30 * (x - 1) + y + 1] = 1
        elif T[x - 1][y + 1] <= 3:
            ans[30 * (x - 1) + y + 1] = (3 - T[x - 1][y + 1] + 3) % 4

        if T[x][y + 2] == 5:
            ans[30 * (x) + y + 2] = 1
        elif T[x][y + 2] <= 3:
            ans[30 * (x) + y + 2] = (3 - T[x][y + 2] + 1) % 4

        if T[x - 1][y + 2] == 4:
            ans[30 * (x - 1) + y + 2] = 1
        elif T[x - 1][y + 2] <= 3:
            ans[30 * (x - 1) + y + 2] = (3 - T[x - 1][y + 2] + 2) % 4

    # 左上
    if T[x][y] == 4 and not T[x - 1][y] in (6, 7) and not T[x][y - 1] in (6, 7) and not T[x - 1][y - 1] in (6, 7):

        ans[30 * (x) + y] = 1

        if T[x - 1][y] == 4:
            ans[30 * (x - 1) + y] = 1
        elif T[x - 1][y] <= 3:
            ans[30 * (x - 1) + y] = (3 - T[x - 1][y] + 2) % 4

        if T[x][y - 1] == 4:
            ans[30 * (x) + y - 1] = 1
        elif T[x][y - 1] <= 3:
            ans[30 * (x) + y - 1] = (3 - T[x][y - 1] + 3) % 4

        if T[x - 1][y - 1] == 5:
            ans[30 * (x - 1) + y - 1] = 1
        elif T[x - 1][y - 1] <= 3:
            ans[30 * (x - 1) + y - 1] = (3 - T[x - 1][y - 1] + 3) % 4

    # 左下
    if (
        T[x + 1][y] == 5
        and not T[x + 2][y] in (6, 7)
        and not T[x + 1][y - 1] in (6, 7)
        and not T[x + 2][y - 1] in (6, 7)
    ):

        ans[30 * (x + 1) + y] = 1

        if T[x + 2][y] == 5:
            ans[30 * (x + 2) + y] = 1
        elif T[x - 1][y] <= 3:
            ans[30 * (x + 2) + y] = (3 - T[x + 2][y] + 1) % 4

        if T[x + 1][y - 1] == 5:
            ans[30 * (x + 1) + y - 1] = 1
        elif T[x + 1][y - 1] <= 3:
            ans[30 * (x + 1) + y - 1] = (3 - T[x + 1][y - 1] + 3) % 4

        if T[x + 2][y - 1] == 4:
            ans[30 * (x + 2) + y - 1] = 1
        elif T[x + 2][y - 1] <= 3:
            ans[30 * (x + 2) + y - 1] = (3 - T[x + 2][y - 1] + 4) % 4

print("".join(map(str, ans)))
