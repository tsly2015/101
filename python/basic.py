wang ~ $ python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print 3
3
>>> print 'hello'
hello
>>> print "hello"
hello
>>> name = 'zhen'
>>> print name[0]
z
>>> print name[1]
h
>>> print name[-1]
n
>>> print name[:100]
zhen
>>> print name[100:]

>>> print name.find('en')
2
>>> print name.find('')
0
>>> name += 'wang'
>>> print name.find('n')
3
>>> print name.find('n', 3)
3
>>> print name.find('n', 4)
6

a, b = 1, 2
s, t = t, s //swap

>>> p=['z','h','e','n']
>>> p[0]
'z'
>>> p[1:3]
['h', 'e']

>>> s = 'Hello'
>>> s[0] = 'Y'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> p = ['H', 'e', 'l', 'l', 'o']
>>> q = p #Aliasing
>>> print p, q
['H', 'e', 'l', 'l', 'o'] ['H', 'e', 'l', 'l', 'o']
>>> p[0] = 'Y'
>>> print p, q

>>> s = 'Hello'
>>> s[0] = 'Y'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> p = ['H', 'e', 'l', 'l', 'o']
>>> q = p #Aliasing
>>> print p, q
['H', 'e', 'l', 'l', 'o'] ['H', 'e', 'l', 'l', 'o']
>>> p[0] = 'Y'
>>> print p, q
['Y', 'e', 'l', 'l', 'o'] ['Y', 'e', 'l', 'l', 'o']

spy = [0,0,7]
def replace_spy(spy):
    spy[2] = spy[2] + 1

>>> def inc(n):
...     n = n + 1
>>> a = 3
>>> inc(a)
>>> print a
3

>>> [0, 1] + [2, 3]
[0, 1, 2, 3]
>>> len([0, 1])
2

>>> p = [1, 2]
>>> q = [3, 4]
>>> p.append(q)
>>> print len(p)
3

>>> 2 ** 10
1024

>>> p = [0, 1, 2, 2, 2]
>>> print p.index(2)
2
>>> print 3 in p
False
>>> print 2 not in p
False