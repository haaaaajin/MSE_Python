리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']  # intra.h, intra.c, define.h, run.py 를 원소로 갖는 리스트를 정함.

for i in 리스트:             # 리스트의 각 원소마다, 아래의 문장들을 실행함. -> 총 4번 실행 할 것임
    split = i.split(".")   # 변수 i에 들어온 원소를, '.' 을 기준으로 나눠서, split이라는 변수에 리스트로 넣음.
    if (split[1] == "h") or (split[1] == "c"):   #만약 split의 1번째(0, 1, 2가 순서) 원소가 'h' 또는 'c'라면, 다음 문장을 실행함.
        print(i)          # print()함수를 사용해 i에 들어간 리스트의 원소를 출력함.