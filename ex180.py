low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000] # 각각 5일간의 저가, 고가 정보가 저장된 리스트 두개를 정한다.

volatility = [ ]     # 비어있는 리스트 volatility를 만든다.
for i in range(5):   # 변수 i에 0부터 4까지 숫자를 차례대로 넣는다.
    변동폭 = high_prices[i] - low_prices[i]  # 변동폭이라는 변수에 i번째 원소의 차를 넣고,
    volatility.append(변동폭)    # 리스트 volatility에 변동폭을 원소로 추가한다.
    
print(volatility)   # for문이 끝나면, print()함수를 사용해 리스트 volatility를 출력한다.