#-*-coding:utf8
#sys 모듈로 부터 exit 를 입력한다
# exit는 프로그램을 그만두는 역할을 한다.
from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"
# 0 이라는 문자와 1이라은 문자가 들어있으면 (여기서 int는 문자열을 숫자열(정수)로 치환을 해주는 기능을한다)
# how_much 에서 숫자열로 인식하게끔 한다.
#추가로 float는 소수점아래(실수)범위까지 입력이 가능하게끔 한다.
    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
#그렇지 않다면 else,
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")
        #스위치 캔슬 블락(swich-case block)
        #choice 에 의한 함수 정의
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

#recursion 살피기.
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
#함수를 이용하게 되면 게임의 확장이 쉬워진다.