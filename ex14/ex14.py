from sys import argv

script,kangeun = argv
prompt = '>'

print ("Hi %s,I'm the %s script." % (kangeun,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % kangeun)
likes = raw_input(prompt)
print("Where do you live %s?" % kangeun)
lives = raw_input(prompt)

print("what kind of computer do you have?")
computer = raw_input(prompt)

print ("""
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
"""% (likes,lives,computer))