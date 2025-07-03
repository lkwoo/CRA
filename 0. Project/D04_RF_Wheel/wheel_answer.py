def get_1000_dollar(board, chance, ffirst, user_char):
    result = 0
    for line in range(len(board)):
        for x in range(len(board[line])):
            # 만약 퀴즈참가자가 요청한 문자가,
            # 정답 문자열과 동일하다면
            if board[line][x] == user_char:
                # lets first 점수인지 확인한다.
                if ffirst[line] == 0 and x == 0:
                    result += 1000
                    ffirst[line] = 1
                    chance[line] = line
                elif ffirst[line] == 0 and x != 0:
                    ffirst[line] = 1
    return result


def get_2000_dollar(board, chance, user_char):
    result = 0
    for line in range(len(board)):
        if chance[line] == -1: continue
        chance[line] = -1

        for x in range(len(board[line])):
            if board[line][x] != user_char:
                continue
            result += 2000
            break

    return result