class OMG :         # OMG라는 class를 생성한다.
    def print() :   # 클래스 안에는 print()라는 함수가 새로 정의 되는데,
        print("Oh my god")  # 이 함수는 "Oh my god"을 출력한다.

mystock = OMG()     # 클래스 OMG를 mystock이라는 변수로 바인딩한다.
mystock.print()     # mystock.print()는 파이썬이 OMG.print(mystock)으로 전달하게 된다.
  # 이때 OMG클래스 안의 함수에는 변수를 받을 수 있는 인자가 없으므로 에러가 발생한다.
  # OMG 클래스에서 함수를 실행하고 싶으면, OMG.print() 라고 코드를 작성하면, 'Oh my god'이 출력된다.