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
print ' '.join(stuff)
print '#'.join(stuff[3:5])
