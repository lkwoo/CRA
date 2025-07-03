# str에서 특정 index 문자만 변경
# 예시 : "____"에서 2번 index 문자를 Q로 변경
# replace_chat_at("____", 2, 'Q')  # 결과 : "__Q_"
def replace_char_at(text, index, new_char):
    return text[:index] + new_char + text[index + 1:]


def get_second_chance_reward(board_map, strs, chance, user_char):
    LETS_SECOND_REWARD = 2000
    res = 0

    for y in range(len(strs)):
        if chance[y] != -1:
            for x in range(len(strs[y])):
                if board_map[y][x] == 0 and strs[y][x] == user_char:
                    print(f"get second change reward! y: {y}, char: {user_char}")
                    chance[y] = -1
                    res += LETS_SECOND_REWARD
                    break
            chance[y] = -1

    return res

def get_first_chance_reward(board_map, strs, chance, user_char, ffirst):
    LETS_FIRST_REWARD = 1000
    res = 0

    for y in range(len(strs)):
        for x in range(len(strs[y])):
            if board_map[y][x] == 1:
                continue

            if strs[y][x] == user_char and ffirst[y] == 0 and x == 0:
                chance[y] = 1
                print(f"get first change reward! char: {user_char}, y: {y}")
                res += LETS_FIRST_REWARD

    return res

def get_award(strs, userdata):
    board_map = [[0 for _ in range(15)] for _ in range(4)]
    consecution_cnt = 0
    ffirst = [0] * 4
    sum = 0
    chance = [-1] * 4

    # 하나씩 처리
    # 26글자 for문 돌면서 퀴즈 참석자가 하나씩 시도를 하는 것
    for i in range(len(userdata)):
        second_chance_reward = get_second_chance_reward(board_map, strs, chance, userdata[i])
        first_chance_reward = get_first_chance_reward(board_map, strs, chance, userdata[i], ffirst)
        sum += first_chance_reward + second_chance_reward

        pass_cnt = 0
        for y in range(len(strs)):
            for x in range(len(strs[y])):
                if board_map[y][x] == 1:
                    continue

                if strs[y][x] == userdata[i]:
                    ffirst[y] = 1
                    board_map[y][x] = 1

                    strs[y] = replace_char_at(strs[y], x, '_')
                    pass_cnt += 1

        if pass_cnt:
            consecution_cnt += 1
            sum += (consecution_cnt * 100) * pass_cnt
        else:
            consecution_cnt = 0
            chance = [-1] * 4

        print(f"userchar: {userdata[i]}, sum: {sum}, strs")

    return sum