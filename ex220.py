def print_max(a, b, c):   # 가장 큰 값을 출력해주는 print_max()함수를 정의한다.
    max_value = a         # max_value라는 변수에, 초기값을 a로 설정한다.
    if b > max_value :    # b값이 max_value보다 크면, max_value에 b값을 저장한다.
        max_value = b     # 그렇지 않으면 다음 if문으로 넘어간다.
    if c > max_value :    # c값이 max_value보다 크면, max_value에 c값을 저장한다.
        max_value = c     # 그렇지 않으면 다음 문장으로 넘어간다.
    print(max_value)      # print()함수를 이용해 최종으로 저장된 max_value값을 출력한다.

print_max(-4, -8, 2)     #print_max() 함수의 사용 예시이다!