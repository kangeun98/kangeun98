Python 2.7.11 |Anaconda 2.5.0 (64-bit)| (default, Jan 29 2016, 14:26:21) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> formatter = "%r %r %r %r"
>>> 
>>> print formatter % (1, 2, 3, 4)
1 2 3 4
>>> print formatter % ("one", "two", "three", "four")
'one' 'two' 'three' 'four'
>>> print formatter % (True, False, False, True)
True False False True
>>> print formatter % (formatter, formatter, formatter, formatter)
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
>>> print formatter % (
"I had this thing.",
 "That you could type up right.",
 "But it didn't sing.",
  "So I said goodnight."
)

'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
>>> 
