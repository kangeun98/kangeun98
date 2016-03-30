Python 2.7.11 |Anaconda 2.5.0 (64-bit)| (default, Jan 29 2016, 14:26:21) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Here's some new strange stuff, remember type it exactly.

>>> days = "Mon Tue Wed Thu Fri sat Sun"
>>> months= "Jan/nFeb/nMar/nApr/nMay/nJun/nJul/nAug"
>>> 
>>> print "Here are the days",days
Here are the days Mon Tue Wed Thu Fri sat Sun
>>> print "Here are the months:".months

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print "Here are the months:".months
AttributeError: 'str' object has no attribute 'months'
>>> print "Here are the months:",months
Here are the months: Jan/nFeb/nMar/nApr/nMay/nJun/nJul/nAug
>>> print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want,or 5, or 6.
"""

There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want,or 5, or 6.

>>> 
