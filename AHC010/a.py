import random

T = [list(map(int,[*input()])) for _ in range(30)]

# print(T)

# ans = "0"*900
ans = "".join([random.choice("0") for _ in range(900)])

for x in range(30):
    for y in range(30):
        # if T[i] == 4 or T[i] == 5:
        # if i + 31 < 900 and (T[i] == 2 or T[i] == 4) and (T[i+1] == 1 or T[i+1] == 5) and (T[i+30] == 3 or T[i+30] == 5) and (T[i+31] == 0 or T[i+31] == 4):
        if (
            x + 1 < 30
            and y + 1 < 30
            and (T[x][y] == 2 or T[x][y] == 4)
            and (T[x][y + 1] == 1 or T[x][y + 1] == 5)
            and (T[x + 1][y] == 3 or T[x + 1][y] == 5)
            and (T[x + 1][y + 1] == 0 or T[x + 1][y + 1] == 4)
        ):

            print(x, y, "loop")

    # print(ans)
