# 아래 2-3번줄의 코드는 requests 모듈을 불러온 후에, 비트고인의 가격 정보를 딕셔너리 btc로 가져온다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# 아래 6-8번줄의 코드는, float()을 이용해 딕셔너리 btc 안의 실수값인 value값을 가져와 각각 변동폭, 시가, 최고가 라는 변수에 저장한다.
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가 + 변동폭) > 최고가 :  # 처음에 딕셔너리 btc에 불러온 값을 이용해서, (시가 + 변동폭)이 최고가보다 값이 크다면,
    print("상승장")         # if문 내의 print()함수를 이용해 '상승장'을 결과값으로 출력한다.
else :                    # "(시가 + 변동폭) > 최고가" 가 성립하지 않는다면, 
    print("하락장")         # else문 내의 print()함수를 이용해 '하락장'을 결과값으로 출력한다.