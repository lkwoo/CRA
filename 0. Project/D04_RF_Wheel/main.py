from wheel import get_award

# 파일 입력
# input1.txt 파일을 읽어와 객체에 값 세팅
with open('input2.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]

n = int(lines[0])
strs = lines[1:1+n]
userdata = lines[1+n]

sum = get_award(strs, userdata)
print("$" + str(sum))