# 271 ~ 280
import datetime
import random

class Account:
    count = 0

    def __init__(self, name, balance):
        self.bank = 'SC은행'
        self.name = name
        self.balance = balance

        self.deposit_count = 0
        self.withdraw_count = 0

        self.deposit_history = []
        self.withdraw_history = []

        aaa = str(random.randint(0, 999)).zfill(3)
        bb = str(random.randint(0, 99)).zfill(2)
        cccccc = str(random.randint(0, 999999)).zfill(6)
    
        self.account = f'{aaa}-{bb}-{cccccc}'

        Account.count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1

            now = datetime.datetime.now()
            self.deposit_history.append({
                'date': now.strftime('%Y-%m-%d %H:%M'),
                'amount': amount
            })

            if self.deposit_count % 5 == 0:
                self.balance *= 1.01

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.withdraw_count += 1

            now = datetime.datetime.now()
            self.withdraw_history.append({
                'date': now.strftime('%Y-%m-%d %H:%M'),
                'amount': amount
            })

    def display_info(self):
        print('은행이름:', self.bank)
        print('예금주:', self.name)
        print('계좌번호:', self.account)
        print('잔고:', f'{self.balance:,}')

    def display_deposit_history(self):
        print(self.deposit_history)

    def display_withdraw_history(self):
        print(self.withdraw_history)

alice = Account('alice', 100000)
bob = Account('bob', 1000)
charlie = Account('charlie', 10)

accountlist = [alice, bob, charlie]

for account in accountlist:
    if account.balance >= 1000000:
        account.display_info()


alice.withdraw(100)
alice.withdraw(10)
alice.withdraw(10)

alice.display_info()
alice.display_withdraw_history()