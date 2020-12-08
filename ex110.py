if True :            # 처음 주어진 조건이 True이기 때문에, 7-8번줄의 else는 실행되지 않고, 1-6번줄의 if문이 실행된다.
    if False:        # 처음 주어진 조건은 True이므로, 2-4번줄의 if문은 실행되지 않고, 5-6번줄의 else문이 실행된다.
        print("1")
        print("2")
    else:            # print()함수를 사용하여 '3'이 출력된다.
        print("3")
else :               # 가장 큰 if-else블럭에서 if문이 실행됐으므로, 7-8번줄의 else문은 실행되지 않는다.
    print("4")
print("5")           # if-else문을 빠져나온 후, print()함수가 있으므로, print()함수를 사용하여 '5'가 출력된다.

# 따라서 이 코드에 의해 3과 5가 차례로 출력될 것이다.