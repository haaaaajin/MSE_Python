# 아래의 코드를 실행하면, '자식생성'이 출력되고, 그 다음으로 '부모생성'이 출력될 것이다.

class 부모 :     # 클래스 '부모'를 생성함.
    def __init__(self):  # 클래스 '부모'의 객체가 생성 될 때, 다음을 자동으로 실행한다.
        print("부모생성")  # print()함수를 이용해 '부모생성'이라는 문자를 출력한다.


class 자식(부모):    # 클래스 '부모'를 상속받은 클래스 '자식'을 생성함.
    def __init__(self):   # 클래스 '자식'의 객체가 생성 될 때, 다음을 자동으로 실행함.
        print("자식생성")    # print()함수를 이용해 '자식생성'이라는 문자를 출력하고,
        super().__init__() # 상속 받은 클래스(부모)의 생성자를 가져와 그대로 실행한다. 이 코드에서는 print()함수를 이용하여 '부모생성'이라는 문자가 출력된다.


나 = 자식()