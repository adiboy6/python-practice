# LISTS - mutable
# map usage
squares = list(map(lambda x: x ** 2, range(10)))

# simplified form of the above using List Comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

result = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(result)

"""
Equivalent to:
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
"""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Nested List Comprehension to transpose above matrix
print([[row[i] for row in matrix] for i in range(4)])

# TUPLE - immutable
t = 12345, 54321, 'hello!'
print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

# empty tuple where len is 0
empty = ()
print(empty)

# trailing comma means, it's a tuple
singleton = 'hello',
print(singleton)

# unpacking a tuple
x, y, z = t

# SET

# empty set
basket = set()

# set comprehension
a = {x for x in 'abracadabra'}
print(a)

# DICTIONARY

"""
Tuples which contains only strings, numbers, or tuples can be used as a key since it's immutable.
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key
"""

# dictionary comprehension
dictionary = {x: x ** 2 for x in (2, 4, 6)}

print(dict(sape=4139, guido=4127, jack=4098))

for key, value in dictionary.items():
    print(key, value)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
