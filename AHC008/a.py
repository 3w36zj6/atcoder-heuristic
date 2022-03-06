N = int(input())
pets = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
humans = [list(map(int, input().split())) for _ in range(M)]

# 30x30
# 1-30

state = [0 for _ in range(M)]
cancel = [False for _ in range(M)]

impassable = [[False for _ in range(32)] for _ in range(32)]
can_construct = [[True for _ in range(32)] for _ in range(32)]
for i in range(N):
    can_construct[pets[i][0]][pets[i][1]] = False

for turn in range(300):

    answer = ["." for _ in range(M)]

    for i in range(5, M):
        if humans[i][0] != 15 and humans[i][1] % 3 == 2:
            answer[i] = "R"
            humans[i][1] += 1
        elif 1 < humans[i][0] <= 15:
            answer[i] = "U"
            humans[i][0] -= 1
        elif humans[i][0] < 30:
            answer[i] = "D"
            humans[i][0] += 1

    for i in range(5):
        pass
        if state[i] == 0 and humans[i][1] < 3 + 6 * i:  # Y座標
            answer[i] = "R"
            humans[i][1] += 1
        elif state[i] == 0 and humans[i][1] > 3 + 6 * i:
            answer[i] = "L"
            humans[i][1] -= 1
        elif state[i] == 0 and humans[i][0] > 1:  # X座標
            answer[i] = "U"
            humans[i][0] -= 1
        elif state[i] == 0 and humans[i][0] == 1:
            if (
                can_construct[humans[i][0]][humans[i][1] - 1]
                and can_construct[humans[i][0]][humans[i][1] - 2]
                and can_construct[humans[i][0] + 1][humans[i][1] - 1]
                and can_construct[humans[i][0] - 1][humans[i][1] - 1]
                and can_construct[humans[i][0]][humans[i][1]]
                and turn >= 30
            ):
                state[i] = 1
                answer[i] = "l"
                impassable[humans[i][0]][humans[i][1] - 1] = True
                # humans[i][0] += 1
        elif state[i] == 1 and humans[i][0] < 30:
            if impassable[humans[i][0]][humans[i][1] - 1] or 14 <= humans[i][0] <= 16:
                answer[i] = "D"
                humans[i][0] += 1
            else:
                if (
                    can_construct[humans[i][0]][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1] - 2]
                    and can_construct[humans[i][0] + 1][humans[i][1] - 1]
                    and can_construct[humans[i][0] - 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    answer[i] = "l"
                    impassable[humans[i][0]][humans[i][1] - 1] = True
        elif state[i] == 1 and humans[i][0] == 30:
            if impassable[humans[i][0]][humans[i][1] - 1] or humans[i][0] == 15:
                answer[i] = "R"
                humans[i][1] += 1
                state[i] = 2
            else:
                if (
                    can_construct[humans[i][0]][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1] - 2]
                    and can_construct[humans[i][0] + 1][humans[i][1] - 1]
                    and can_construct[humans[i][0] - 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    answer[i] = "l"
                    impassable[humans[i][0]][humans[i][1] - 1] = True
        elif state[i] == 2 and humans[i][0] > 1:
            if impassable[humans[i][0]][humans[i][1] + 1] or 14 <= humans[i][0] <= 16:
                answer[i] = "U"
                humans[i][0] -= 1
            else:
                if (
                    can_construct[humans[i][0]][humans[i][1] + 1]
                    and can_construct[humans[i][0]][humans[i][1] + 2]
                    and can_construct[humans[i][0] + 1][humans[i][1] + 1]
                    and can_construct[humans[i][0] - 1][humans[i][1] + 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    answer[i] = "r"
                    impassable[humans[i][0]][humans[i][1] + 1] = True
        elif state[i] == 2 and humans[i][0] == 1:
            if (
                can_construct[humans[i][0]][humans[i][1] + 1]
                and can_construct[humans[i][0]][humans[i][1] + 2]
                and can_construct[humans[i][0] + 1][humans[i][1] + 1]
                and can_construct[humans[i][0] - 1][humans[i][1] + 1]
                and can_construct[humans[i][0]][humans[i][1]]
            ):
                answer[i] = "r"
                impassable[humans[i][0]][humans[i][1] + 1] = True
                state[i] = 3
        elif state[i] == 3 and humans[i][0] != 15:
            answer[i] = "D"
            humans[i][0] += 1
        elif state[i] == 3 and humans[i][0] == 15:
            state[i] = 4

        if state[i] == 4:
            for j in range(12):
                if (
                    (not can_construct[12 - j][4 + 6 * i] or not can_construct[12 - j][4 + 6 * i - 1])
                    and not impassable[14][4 + 6 * i]
                    and not impassable[14][4 + 6 * i - 1]
                ):
                    state[i] = 5  # 上を埋める
                    break
                if (
                    (not can_construct[18 + j][4 + 6 * i] or not can_construct[18 + j][4 + 6 * i - 1])
                    and not impassable[16][4 + 6 * i]
                    and not impassable[16][4 + 6 * i - 1]
                ):
                    state[i] = 6  # 下を埋める
                    break
                if not can_construct[12 - j][1 + 6 * i] and not impassable[14][1 + 6 * i]:
                    state[i] = 7  # 左上を埋める
                    break
                if not can_construct[18 + j][1 + 6 * i] and not impassable[16][1 + 6 * i]:
                    state[i] = 8  # 左下を埋める
                    break
                if not can_construct[12 - j][1 + 6 * i + 5] and not impassable[14][1 + 6 * i + 5]:
                    state[i] = 9  # 右上を埋める
                    break
                if not can_construct[18 + j][1 + 6 * i + 5] and not impassable[16][1 + 6 * i + 5]:
                    state[i] = 10  # 右下を埋める
                    break

        if state[i] == 4:
            if turn >= 220:
                if not impassable[14][4 + 6 * i]:
                    state[i] = 11  # 上に移動して犬をひきつける
                elif not impassable[16][4 + 6 * i]:
                    state[i] = 13  # 下に移動して犬をひきつける

        if state[i] == 11:
            if humans[i][0] != 11:
                answer[i] = "U"
                humans[i][0] -= 1
            else:
                state[i] = 12  # 下に戻る

        if state[i] == 12:
            if humans[i][0] != 15:
                answer[i] = "D"
                humans[i][0] += 1
            else:
                state[i] = 4

        if state[i] == 13:
            if humans[i][0] != 19:
                answer[i] = "D"
                humans[i][0] += 1
            else:
                state[i] = 14  # 上に戻る

        if state[i] == 14:
            if humans[i][0] != 15:
                answer[i] = "U"
                humans[i][0] -= 1
            else:
                state[i] = 4

        if state[i] == 5:
            pass
            if humans[i][1] == 4 + 6 * i:
                if impassable[humans[i][0] - 1][humans[i][1]]:
                    answer[i] = "L"
                    humans[i][1] -= 1
                elif (
                    can_construct[humans[i][0] - 1][humans[i][1]]
                    and can_construct[humans[i][0] - 2][humans[i][1]]
                    and can_construct[humans[i][0] - 1][humans[i][1] + 1]
                    and can_construct[humans[i][0] - 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    answer[i] = "u"
                    impassable[humans[i][0] - 1][humans[i][1]] = True
            else:
                if impassable[humans[i][0] - 1][humans[i][1]] or cancel[i]:
                    answer[i] = "R"
                    humans[i][1] += 1
                    state[i] = 4
                    cancel[i] = False
                elif (
                    can_construct[humans[i][0] - 1][humans[i][1]]
                    and can_construct[humans[i][0] - 2][humans[i][1]]
                    and can_construct[humans[i][0] - 1][humans[i][1] + 1]
                    and can_construct[humans[i][0] - 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    for j in range(12):
                        if not can_construct[12 - j][4 + 6 * i] or not can_construct[12 - j][4 + 6 * i - 1]:
                            answer[i] = "u"
                            impassable[humans[i][0] - 1][humans[i][1]] = True
                            break
                    else:
                        cancel[i] = True

        if state[i] == 6:
            pass
            if humans[i][1] == 4 + 6 * i:
                if impassable[humans[i][0] + 1][humans[i][1]]:
                    answer[i] = "L"
                    humans[i][1] -= 1
                elif (
                    can_construct[humans[i][0] + 1][humans[i][1]]
                    and can_construct[humans[i][0] + 2][humans[i][1]]
                    and can_construct[humans[i][0] + 1][humans[i][1] + 1]
                    and can_construct[humans[i][0] + 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    answer[i] = "d"
                    impassable[humans[i][0] + 1][humans[i][1]] = True
            else:
                if impassable[humans[i][0] + 1][humans[i][1]] or cancel[i]:
                    answer[i] = "R"
                    humans[i][1] += 1
                    state[i] = 4
                    cancel[i] = False
                elif (
                    can_construct[humans[i][0] + 1][humans[i][1]]
                    and can_construct[humans[i][0] + 2][humans[i][1]]
                    and can_construct[humans[i][0] + 1][humans[i][1] + 1]
                    and can_construct[humans[i][0] + 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    for j in range(12):
                        if not can_construct[18 + j][4 + 6 * i] or not can_construct[18 + j][4 + 6 * i - 1]:
                            answer[i] = "d"
                            impassable[humans[i][0] + 1][humans[i][1]] = True
                            break
                    else:
                        cancel[i] = True

        if state[i] == 7:
            if humans[i][1] > 4 + 6 * i - 3 and not impassable[humans[i][0] - 1][4 + 6 * i - 3] and not cancel[i]:
                if not impassable[humans[i][0] - 1][4 + 6 * i - 3]:
                    answer[i] = "L"
                    humans[i][1] -= 1
            elif humans[i][1] == 4 + 6 * i - 3 and not impassable[humans[i][0] - 1][4 + 6 * i - 3] and not cancel[i]:
                if (
                    can_construct[humans[i][0] - 1][humans[i][1]]
                    and can_construct[humans[i][0] - 2][humans[i][1]]
                    and can_construct[humans[i][0] - 1][humans[i][1] + 1]
                    and can_construct[humans[i][0] - 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    for j in range(12):
                        if not can_construct[12 - j][1 + 6 * i] or not can_construct[12 - j][1 + 6 * i - 1]:
                            answer[i] = "u"
                            impassable[humans[i][0] - 1][humans[i][1]] = True
                            break
                    else:
                        cancel[i] = True

            elif humans[i][1] != 4 + 6 * i and (impassable[humans[i][0] - 1][4 + 6 * i - 3] or cancel[i]):
                answer[i] = "R"
                humans[i][1] += 1
            else:
                state[i] = 4
                cancel[i] = False

        if state[i] == 8:
            if humans[i][1] > 4 + 6 * i - 3 and not impassable[humans[i][0] + 1][4 + 6 * i - 3] and not cancel[i]:
                if not impassable[humans[i][0] + 1][4 + 6 * i - 3]:
                    answer[i] = "L"
                    humans[i][1] -= 1
            elif humans[i][1] == 4 + 6 * i - 3 and not impassable[humans[i][0] + 1][4 + 6 * i - 3] and not cancel[i]:
                if (
                    can_construct[humans[i][0] + 1][humans[i][1]]
                    and can_construct[humans[i][0] + 2][humans[i][1]]
                    and can_construct[humans[i][0] + 1][humans[i][1] + 1]
                    and can_construct[humans[i][0] + 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    for j in range(12):
                        if not can_construct[18 + j][1 + 6 * i] or not can_construct[18 + j][1 + 6 * i - 1]:
                            answer[i] = "d"
                            impassable[humans[i][0] + 1][humans[i][1]] = True
                            break
                    else:
                        cancel[i] = True
            elif humans[i][1] != 4 + 6 * i and (impassable[humans[i][0] + 1][4 + 6 * i - 3] or cancel[i]):
                answer[i] = "R"
                humans[i][1] += 1
            else:
                state[i] = 4
                cancel[i] = False

        if state[i] == 9:
            if humans[i][1] < 4 + 6 * i + 2 and not impassable[humans[i][0] - 1][4 + 6 * i + 2] and not cancel[i]:
                if not impassable[humans[i][0] - 1][4 + 6 * i + 2]:
                    answer[i] = "R"
                    humans[i][1] += 1
            elif humans[i][1] == 4 + 6 * i + 2 and not impassable[humans[i][0] - 1][4 + 6 * i + 2] and not cancel[i]:
                if (
                    can_construct[humans[i][0] - 1][humans[i][1]]
                    and can_construct[humans[i][0] - 2][humans[i][1]]
                    and can_construct[humans[i][0] - 1][humans[i][1] + 1]
                    and can_construct[humans[i][0] - 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    for j in range(12):
                        if not can_construct[12 - j][4 + 6 * i + 2] or not can_construct[12 - j][4 + 6 * i + 2 + 1]:
                            answer[i] = "u"
                            impassable[humans[i][0] - 1][humans[i][1]] = True
                            break
                    else:
                        cancel[i] = True
            elif humans[i][1] != 4 + 6 * i and (impassable[humans[i][0] - 1][4 + 6 * i + 2] or cancel[i]):
                answer[i] = "L"
                humans[i][1] -= 1
            else:
                state[i] = 4
                cancel[i] = False

        if state[i] == 10:
            if humans[i][1] < 4 + 6 * i + 2 and not impassable[humans[i][0] + 1][4 + 6 * i + 2] and not cancel[i]:
                if not impassable[humans[i][0] + 1][4 + 6 * i + 2]:
                    answer[i] = "R"
                    humans[i][1] += 1
            elif humans[i][1] == 4 + 6 * i + 2 and not impassable[humans[i][0] + 1][4 + 6 * i + 2] and not cancel[i]:
                if (
                    can_construct[humans[i][0] + 1][humans[i][1]]
                    and can_construct[humans[i][0] + 2][humans[i][1]]
                    and can_construct[humans[i][0] + 1][humans[i][1] + 1]
                    and can_construct[humans[i][0] + 1][humans[i][1] - 1]
                    and can_construct[humans[i][0]][humans[i][1]]
                ):
                    for j in range(12):
                        if not can_construct[18 + j][4 + 6 * i + 2] or not can_construct[18 + j][4 + 6 * i + 2 + 1]:
                            answer[i] = "d"
                            impassable[humans[i][0] + 1][humans[i][1]] = True
                            break
                    else:
                        cancel[i] = True
            elif humans[i][1] != 4 + 6 * i and (impassable[humans[i][0] + 1][4 + 6 * i + 2] or cancel[i]):
                answer[i] = "L"
                humans[i][1] -= 1
            else:
                state[i] = 4
                cancel[i] = False

    print("".join(answer))

    pet_input = input().split()

    can_construct = [[True for _ in range(32)] for _ in range(32)]  # init
    for i in range(N):
        dx = dy = 0
        for pet_move in pet_input[i]:
            if pet_move == "D":
                dx += 1
            elif pet_move == "U":
                dx -= 1
            elif pet_move == "R":
                dy += 1
            elif pet_move == "L":
                dy -= 1

        can_construct[pets[i][0] + dx][pets[i][1] + dy] = False
        pets[i][0] += dx
        pets[i][1] += dy
