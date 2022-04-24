import random

T = [list(map(int,[*input()])) for _ in range(30)]

# print(T)

# ans = "0"*900
ans = [0 for _ in range(900)]

mini_loops = []

for x in range(30):
    for y in range(30):
        # if T[i] == 4 or T[i] == 5:
        # if i + 31 < 900 and (T[i] == 2 or T[i] == 4) and (T[i+1] == 1 or T[i+1] == 5) and (T[i+30] == 3 or T[i+30] == 5) and (T[i+31] == 0 or T[i+31] == 4):
        if (
            x + 2 < 30
            and y + 2 < 30
            and (T[x][y] == 2 or T[x][y] == 4)
            and (T[x][y + 1] == 1 or T[x][y + 1] == 5)
            and (T[x + 1][y] == 3 or T[x + 1][y] == 5)
            and (T[x + 1][y + 1] == 0 or T[x + 1][y + 1] == 4)
        ):

            #print(x, y, "loop")
            mini_loops.append((x, y))


    # print(ans)

#print(mini_loops)

for loop in mini_loops:
    #print(loop)
    x, y = loop
    # 左下
    if T[x+1][y+1] == 4 and not T[x+2][y+1] in (6,7) and not T[x+1][y+2] in (6,7) and not T[x+2][y+2] in (6,7):
        #print(loop)

        ans[30*(x+1)+y+1] = 1

        if T[x+2][y+1] == 4:
            ans[30*(x+2)+y+1] = 1
        elif T[x+2][y+1] <= 3:
            ans[30*(x+2)+y+1] = 3 - T[x+2][y+1]

        if T[x+1][y+2] == 4:
            ans[30*(x+1)+y+2] = 1
        elif T[x+1][y+2] <= 3:
            ans[30*(x+1)+y+2] = (3 - T[x+1][y+2]+2)%4

        if T[x+2][y+2] == 5:
            ans[30*(x+2)+y+2] = 1
        elif T[x+2][y+2] <= 3:
            ans[30*(x+2)+y+2] = (3 - T[x+2][y+2]+1)%4

print("".join(map(str,ans)))