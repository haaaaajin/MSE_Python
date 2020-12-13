# 아래의 코드를 실행하면, 'B C B C B C A'가 출력될 것이다.

def message1():   # message1()라는 함수를 실행하면,
    print("A")    # print()함수를 이용해 'A'를 출력한다.

def message2():   # message2()라는 함수를 실행하면,
    print("B")    # print()함수를 이용해 'B'를 출력한다.

def message3():           # message3()라는 함수를 실행하면,
    for i in range (3) :  # 변수 i에 0, 1, 2가 차례로 들어가 총 3번 for문이 실행된다.  
        message2()        # message2()함수를 실행해서 'B'를 출력한다.
        print("C")        # print()함수를 이용해서 'C'를 출력한다.
    message1()            # for문 실행이 끝나면, message1()함수를 실행해서 'A'를 출력한다.

message3()    # message3() 함수를 실행한다. 9-13번줄을 실행해서, 'B C B C B C A'가 출력될 것이다.