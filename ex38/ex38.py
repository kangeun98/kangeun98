#-*-coding:utf8
#디버깅 해보기.
#디버깅으로 코딩문들을 살펴보기.
#ten_things 라는 문자열을 spilt를함 ' ' 라는 문자열로 구분함으로
ten_things="Appels Oranges Crows Telephone light sugar"
print"wait there are not 10 things in that list. let's fix that."

stuff=ten_things.split(' ')
more_stuff=["Day","Night","song","Frisbee","Corn","Banana","Girl","Boy"]
while len(stuff) !=10:
    next_one=more_stuff.pop()
    print "Adding:",next_one
    stuff.append(next_one)
    print "There are %d items now."% len(stuff)

print"There we go:",stuff
print"Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
#스페이스(띄우기) join 관계 와 # 과 join의 관계 결과살피기.
#서로 문자열을 잇는 역할을 해준다 (붙이기)
print ' '.join(stuff)
print '#'.join(stuff[3:5])
