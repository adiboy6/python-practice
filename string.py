# add raw string instead of adding backslash(/)
print(r'C:\some\name')

# multi-line string literal can be achieved by using ("""...""") or ('''...''')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# String literals can be divided if it's large
print('Py''thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

random_string = 'hello'

# only works with two literals though, not with variables or expressions:
# print(random_string'world')

# string is immutable
'''
>>>x="hi"
>>>x[0]="g" #not possbile
'''