ohlc = [ ["open", "high", "low", "close"], [100, 110, 70,100], [200, 210, 180, 190], [300, 310, 300, 310]]
# 3일간의 ohlc데이터를 원소로 가지고 있는 리스트 ohlc를 지정한다. ohlc의 원소들은, 각각 시가, 최고가, 최저가, 종가를 원소로 하는 리스트이다.

total = 0     # 총 수익금을 저장할 변수 total의 초기값을 0으로 정한다.
for i in ohlc[1:]:      # 리스트 ohlc를 슬라이싱해, 1번째 원소부터 변수 i에 넣는다.
    수익금 = i[3] - i[0]  # 수익금이라는 변수는, 변수 i에 있는 리스트 중, 3번째 원소 와 0번째 원소의 차이를 그 값으로 가진다.
    total += 수익금       # total값에 위에서 정해진 수익금 변수를 더해서 다시 total에 저장한다.
print(total)       # for문이 다 끝나cd면, print()함수를 이용해서 total값을 출력한다.