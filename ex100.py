date = ['09/05', '09/06', '09/07', '09/08', '09/09']  # '09/05', '09/06', '09/07', '09/08', '09/09' 를 원소로 가지는 리스트 date를 생성
close_price = [10500, 10300, 10100, 10800, 11000]     # 10500, 10300, 10100, 10800, 11000를 원소로 가지는 리스트 close_price를 생성
close_table = dict(zip(date, close_price))    # zip()함수와 dict()함수를 이용하여 date를 key로, close_price를 value로 가지는 딕셔너리 close_table을 생성
print(close_table)   # print()함수를 사용하여 딕셔너리 close_table을 출력