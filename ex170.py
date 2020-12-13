num = 1  # num이라는 변수에 가장 먼저 1을 지정해줌.

for i in range(1, 11) :  # range(n, m, l) 함수는, n부터 m-1까지 l의 간격으로 나타내라는 뜻으로, 여기서는 1부터 10까지 차례로 변수 i에 넣는다는 의미이다.
    num = num * i        # num과 i를 곱하고, 그 값을 다시 num에 넣는다. for문을 range함수가 끝날 때까지 반복한다.
print(num)               # for문이 끝나면, print()함수를 이용해 최종 num값을 출력한다.