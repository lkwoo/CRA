def is_valid(text):
    is_there_invalid_char = 0
    cnt_plus = 0
    cnt_equal = 0
    last_plus_index = 0
    last_equal_index = 0

    # +와 = 개수 확인
    for i in range(len(text)):
        if text[i] == "+":
            cnt_plus += 1
            last_plus_index = i
        elif text[i] == "=":
            cnt_equal += 1
            last_equal_index = i
        elif not text[i].isdigit():
            is_there_invalid_char = 1
            break

    if cnt_plus != 1 or cnt_equal != 1 \
            or last_plus_index >= last_equal_index - 1 \
            or is_there_invalid_char\
            or last_plus_index < 1 \
            or last_equal_index < 3 \
            or last_equal_index == len(text) - 1:
        return False

    return True


def get_result(text):
    if not is_valid(text):
        return "ERROR"

    idx_plus = text.find("+")
    idx_equal = text.find("=")

    num1 = text[0:idx_plus]
    num2 = text[idx_plus + 1:idx_equal]
    num3 = text[idx_equal + 1:]

    n1 = int(num1)
    n2 = int(num2)
    n3 = int(num3)

    if n1 + n2 == n3:
        return "PASS"
    else:
        return "FAIL"


# 25+61=100
# 1 ~ 5자리수 덧셈 수식이 맞는지 확인하는 프로그램
# 띄어쓰기 없음
# str = "25+61=86"  # PASS
# str = "12345+12345=24690" # PASS
# str = "5++5=10" # ERROR
# str = "12345+=123" # ERROR
# str = "10000+1=10002" # FAIL

print(get_result(str))
