import numpy     # numpy모듈을 불러온다
for i in numpy.arange(0, 5.1, 0.1):   #numpy의 arange()함수를 이용해 각각의 값을 변수 i에 넣고, 매 회마다 print()함수를 이용해 i를 출력한다.
    print(i)           # arange()함수는 range()함수와 비슷하다. 차이점은 range()함수는 정수만 출력할 수 있다는 것이고, arange()함수는 소숫점 단위도 출력이 가능하다는 것이다.