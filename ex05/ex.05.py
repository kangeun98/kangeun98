Python 3.5.1 |Anaconda 2.4.1 (64-bit)| (default, Dec  7 2015, 15:00:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_name=('zed A. Shaw')
>>> my_age= 35 # not a lie
>>> my_height= 74 # inches
>>> my_weight=180 # Ibs
>>> my_eyes='Blus'
>>> my_teeth='white'
>>> my_hair='Brown'
>>> 
>>> print("Let's talk about %s." % my_name")
      
SyntaxError: EOL while scanning string literal
>>> print("Let's talk about %s.") % my_naem
Let's talk about %s.
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("Let's talk about %s.") % my_naem
NameError: name 'my_naem' is not defined
>>> print("Let's talk about %s.") % my_name
Let's talk about %s.
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("Let's talk about %s.") % my_name
TypeError: unsupported operand type(s) for %: 'NoneType' and 'str'
>>> print("Let's talk about %s."% my_name")
      
SyntaxError: EOL while scanning string literal
>>> print"Let's talk about %s."% my_name"
SyntaxError: invalid syntax
>>> print "Let's talk about %s." % my_name
SyntaxError: Missing parentheses in call to 'print'
>>> print ("Let's talk about %s." % my_name)
Let's talk about zed A. Shaw.
>>> print ("He's %d inches tall." % my_height)
He's 74 inches tall.
>>> print ("He's %d pounds heavy." % my_weight)
He's 180 pounds heavy.
>>> print "Actually that's not too heavy."

SyntaxError: Missing parentheses in call to 'print'
>>> print ("Actually that's not too heavy.")
Actually that's not too heavy.
>>> print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
He's got Blus eyes and Brown hair.
>>> print ("His teeth are usually %s depending on the coffee." % my_teeth)
His teeth are usually white depending on the coffee.
>>> print ("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))
If I add 35, 74, and 180 I get 289.
>>> 
