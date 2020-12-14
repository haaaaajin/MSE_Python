import random   # 모듈 random을 불러옴


class Account:   # 클래스 Account를 생성함.
    account_count = 0   # 클래스 공간 안에 생성된 변수 account_count에 초기값 0을 지정한다.
    
    def __init__(self, name, balance):   # 클래스 Account의 객체가 생성 될 때, 이름과 잔고를 각각 name과 balance라는 변수로 받는다.
        self.deposit_count = 0    # 객체가 생성 될 때, 입금 횟수를 의미하는 변수 deposit_count의 초기값을 0으로 설정한다.
        self.deposit_log = []     # 입금 기록을 저장하는 리스트 생성
        self.withdraw_log = []    # 출금 기록을 저장하는 리스트 생성
        
        self.name = name
        self.balance = balance 
        self.bank = "SC은행"       # 은행 이름은 받는 값과 상관 없이, 전부 'SC은행'이 된다.
        
        # 계좌번호 생성
        num1 = random.randint(0, 999)    # random.radint(a, b) 함수는, a 이상 b 이하의 범위 내에서, 랜덤으로 숫자를 생성할 때 사용한다.
        num2 = random.randint(0, 99)     # num1에는 세자리의 랜덤한 숫자를, num2에는 두자리,
        num3 = random.randint(0, 999999) # num3에는 6자리의 랜덤한 숫자를 생성하고 저장한다.
        
        # 계좌번호 자릿수 맞추기
        num1 = str(num1).zfill(3)   # num1을 문자열로 변경(str)하고, zfill()함수를 사용해서 num1의 숫자를 3자리 숫자로 만든다. (1 -> 001)
        num2 = str(num2).zfill(2)   # num2을 문자열로 변경(str)하고, zfill()함수를 사용해서 num2의 숫자를 2자리 숫자로 만든다. (1 -> 01)
        num3 = str(num3).zfill(6)   # num3을 문자열로 변경(str)하고, zfill()함수를 사용해서 num3의 숫자를 6자리 숫자로 만든다. (106 -> 000106)
        self.account_number = num1 + '-' + num2 + '-' + num3   # 위의 값을 토대로, 계좌번호 'account_number'를 'num1-num2-num3'로 저장한다.

        Account.account_count += 1  # 클래스 변수를 사용해 Account 클래스에서 생성된 계좌 객체의 개수를 저장함.

    @classmethod                  # 객체에 접근할 필요가 없는 것을 클래스매소드라고 부름.
    def get_account_num(cls):     # 매소드 함수 안의 인자가 cls이면, kim.get_account_num()라고 호출을 해도, 변수 자리에 객체 이름이 넘어오지 않고, 클래스의 이름이 넘어온다.
        print(cls.account_count)  # cls.account_count는 Account.account_count라고 작성하는 것과 같다. 현재 클래스에 접근하는 것과 똑같음!

    # 입금
    def deposit(self, amount):        # 통장에 돈을 입금할 때 사용하는 함수를 정의한다. 잔고는 self객체에 저장돼있으므로, 인자에 self를 사용하고, 입금금액은 amount로 받는다.
        if amount >= 1:               # 최소 입금 금액은 1원이므로, if문을 사용하여 amount가 1원 이상일 때, 
            self.balance += amount    # init의 잔고가 balance + amount로 업데이트 된다.
            self.deposit_log.append(amount)   # 입금 금액을 리스트 deposit_log에 저장한다.
            self.deposit_count += 1   # 통장 입금 횟수를 업데이트 한다.

            #이자 지급
            if self.deposit_count % 5 == 0:           # 이때 통장 입금 횟수가 5의 배수이면,
                self.balance = (self.balance * 1.01)  # 그때의 통장잔고를 기준으로 1%의 이자를 받는다. 따라서 통장의 잔고가 self.balance * 1.01 값으로 업데이트 된다.

    # 출금
    def withdraw(self, amount):    # 통장에서 출금을 할 때 사용하는 함수 withdraw를 정의한다. 잔고는 self객체에 저장돼있으므로, 인자에 self를 사용하고, 출금 금액은 amount로 받는다.
        if amount < self.balance:  # 통장 잔고 이상으로는 출금 할 수 없으므로, if문을 사용하여
            self.balance -= amount # amount에 받은 값이 self.balance에 저장된 값보다 작으면, init의 잔고를 balance - amount로 업데이트 한다.
            self.withdraw_log.append(amount) # 출금 금액을 리스트 withdraw_log에 저장한다.

    # 고객정보 보여줌
    def display_info(self):               # Account 인스턴스에 저장된 정보를 출력하는 함수 display_info()를 정의한다.
        print("은행이름 : ", self.bank)     # 이 함수가 실행되면, 객체에 저장돼있는 정보(은행이름, 예금주, 계좌번호, 잔액)를 출력해서 보여준다.
        print("예금주 : ", self.name)
        print("계좌번호 : ", self.account_number)
        print("잔고 : ", self.balance, "원")

    # 입금 기록 보여줌
    def deposit_history(self):            # 클래스 Account에 생성된 리스트 deposit_log에 저장된 입금 기록을 출력하는 함수 deposit_history()를 정의한다.
        print("입금기록")                   # 함수가 실행되면 먼저 print()함수를 이용해 '입금기록'이라는 문자를 출력한다.
        for amount in self.deposit_log :  # 리스트에 속한 원소를 모두 출력할 수 있도록, for문을 사용한다.
            print(amount)                 # for문이 실행되는 동안, 리스트의 원소를 amount에 넣고, 그것을 매 회 출력한다.
            
    # 출금 기록 보여줌
    def withdraw_history(self):            # 클래스 Account에 생성된 리스트 withdraw_log에 저장된 입금 기록을 출력하는 함수 withdraw_history()를 정의한다.
        print("출금기록")                    # 함수가 실행되면 먼저 print()함수를 이용해 '입금기록'이라는 문자를 출력한다.
        for amount in self.withdraw_log:   # 리스트에 속한 원소를 모두 출력할 수 있도록, for문을 사용한다.
            print(amount)                  # for문이 실행되는 동안, 리스트의 원소를 amount에 넣고, 그것을 매 회 출력한다.

k = Account("Kim", 5000)
k.deposit(1500)
k.deposit(500)
k.deposit(1000)
k.deposit_history()

k.withdraw(2000)
k.withdraw(800)
k.withdraw_history()

#객체변수.display_info() ->  Account.display_info(객체변수) Account에 있는 display_info함수를 객체변수에 대해서 호출해라!