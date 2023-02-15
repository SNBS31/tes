Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
\
  'We are the so called "Vikings" from the north.'
SyntaxError: unexpected indent
"We are the so-called \"Vikings\" fron the north"
'We are the so-called "Vikings" fron the north'
"I am \'Ajanoh\'"
"I am 'Ajanoh'"
"This is amazing/awesome"
'This is amazing/awesome'
"This is amazing\awesome"
'This is amazing\x07wesome'
"This is amazing \\ awesome"
'This is amazing \\ awesome'
"This is amazing insert one \\ (backlash)."
'This is amazing insert one \\ (backlash).'


txt = "This will insert one \\ (backlash)."
print(x)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
txt = "I am \\Ajanoh\\"
print(txt)
I am \Ajanoh\
txt = "My name is Salle /n I'm a good boy."
ptin(txt)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    ptin(txt)
NameError: name 'ptin' is not defined. Did you mean: 'print'?
>>> txt = "My name is Salle" /n "I'm a good boy"
SyntaxError: invalid syntax
>>> txt = "My name is Salle/nI'm a good boy!"
>>> print(txt)
My name is Salle/nI'm a good boy!
>>> txt = "Hello\nWorld!"
>>> print(txt)
Hello
World!
>>> txt = "My name is Salle \n I'm a good boy!"
>>> print(txt)
My name is Salle 
 I'm a good boy!
>>> txt = "My name is Salle\nI'm a good boy!"
>>> print(txt)
My name is Salle
I'm a good boy!
>>> txt = "My name is Salle\rI'm a good boy!"
>>> print(txt)
My name is Salle
>>> I'm a good boy!
>>> txt = "Hello\rWorld!"
print(txt)
>>> Hello
>>> World!
txt = "Hello\tWorld!"
>>> print(txt)
>>> Hello	World!
txt = "Hellow\bWorld!"
>>> print(txt)
>>> HellowWorld!
txt = "Hello \bWorld!"
>>> print(txt)
>>> Hello World!
txt = "\231\123\239\237"
