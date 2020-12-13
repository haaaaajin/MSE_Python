# c = 함수2(2)에서, num = 2로 주어졌으므로,
# 함수2()가 실행되면 num = 12로 저장되고, 함수1(12)가 실행된다.
# 함수1()이 실행되면 함수0(num + 2)가 실행되므로, 함수0(14)가 실행된다.
# 함수0()이 실행되면, num 값이 14이므로, 14*2 = 28, 28이 저장된다.
# 따라서 c = 28이고, print()함수에 의해 28이 출력된다.

def 함수0(num) :     # 함수0()을 정의한다.
    return num * 2  # 이 함수는 받은 변수 num에 *2를 한 값을 저장한다.

def 함수1(num) :     # 함수1()을 정의한다.
    return 함수0(num + 2)  # 이 함수는 받은 변수 num에 2를 더한 후, 그것을 함수0()에 넣어 그 결과값을 저장한다.

def 함수2(num) :     # 함수2()를 정의한다.
    num = num + 10  # 이 함수는 받은 변수 num에 10을 더한 후 다시 num에 저장하고,
    return 함수1(num) # 업데이트된 변수 num을 함수1()에 넣어 그 결과값을 저장한다.

c = 함수2(2)   # 1-4번줄에서 설명했듯이, c에는 28이 저장된다.
print(c)      # print()함수에 의해서 c를 출력하면, 28이 출력된다.