fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}  # 봄, 여름, 가을을 key로, 딸기, 토마토, 사과를 각각의 values로 가지는 딕셔너리 fruit를 정의한다.

you = input("좋아하는 과일은?")  # '좋아하는 과일은?'이라는 메시지가 뜨면서, 사용자의 텍스트를 입력받고, 그것을 you라는 변수에 저장한다.
if you in fruit.values() :   # 만약 you에 입력된 문자가 딕셔너리 fruit의 value에 포함되어 있다면, 
    print("정답입니다.")        # if문 안에 있는 print()함수를 실행해 '정답입니다.'를 출력한다.
else :                       # 만약 you에 입력된 문자가 딕셔너리 fruit의 value에 포함되어있지 않다면,
    print("오답입니다.")        # else문 안에 있는 print()함수를 실행해 '오답입니다.'를 출력한다.