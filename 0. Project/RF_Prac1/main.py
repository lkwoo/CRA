def convert_to_f(temp_c):
    return (temp_c * 9 / 5) + 32  # 화씨로 변환

def get_squre_area(length):
    return length * length


temp_c = 24  # 섭씨
temp_f = convert_to_f(temp_c)  # 화씨로 변환
print("섭씨 온도를 화씨로 변환:", temp_f)

length = 10.0  # 길이 (미터)
area = get_squre_area(length)  # 면적 계산
print("정사각형 면적:", area)

