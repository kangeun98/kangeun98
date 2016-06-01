#-*-coding:utf8
balance_won=0 #현금 카드 잔고


#현금 카드로 할 수 있는것:임금,출금,잔고확인

def deposit(amount_won):
    """
     Deposit smoe amount of money into cash card
    """
    #deposit 함수 안의 balance_won 이
    #전역변수임을 표시
    global balance_won

    #임금 하면 잔고가 증가한다
    balance_won+=amount_won

def withdraw(amount_won):
    """
    Withdraw some amount of money from cash card:
    """
    #withdraw 함수 안의 balance_won이
    #전역변수임을 표시
    global balance_won

    # 출금 하면 잔고가 감소한다.
    balance_won += amount_won

def check_balance():
    """
    Check how much is in the cash card:
    """
    #통장 잔고를 반환한다
    #reader function
    return balance_won

#현금 카드 모듈을 불러들임

import Cashcard as Cashcard_module

def chk_bal(message,accout):
    """

    :param message:
    :param accout:
    :return:
    """
    print ("%s : %d"%(message,accout,check_balance()))


#현금 카드 모듈의 잔액확인
chk_bal("CashCard_module 잔액 확인",Cashcard_module)
#현금 카드에 10000원 입금
print "10000원 입금"
# ex09CashCard.py 모듈 안의 deposit() 함수를 호출
# ex09CashCard.py 모듈의 balance_won 값을 읽어 반환
chk_bal("입금 후 잔고 확인".CashCard_module)

#또 다른 현금 카드를 만들수 있을까? 불러 들임
#noinspection PyPep8
import  CashCard as mySistersCard_module

chk_bal("CashCard_module 잔액 확인",Cashcard_module)
chk_bal("mySistersCard_module 잔액 확인",mySistersCard_module)

#그러나 이런 식으로는 한 장의 카드만 만들수 있다

print ("CashCard_module : %s"%Cashcard_module)
print ("mySistersCard_module: %s"% mySistersCard_module)

class SimpleCashCard:
    """
    SimpleCashCard class
    deposit.withdraw.and check_balance methods
    """
    def __init__(self):
        print "SimpleCashCard __init__()"# 함수 호출 표식
        #클래스 생성자(컨스터럭터)
        #멤버 변수 초기화
        # 각 카드 별로 따로 잔고를 기록한다
        self.balance_won=0
        #메소드 mathods :# 객체에 어떤 신호를 전달하는 역할을 한다

