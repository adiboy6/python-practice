import math
import json

# Output Formatting

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
"""
use { and } to mark where a variable will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information to be formatted
"""
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

"""
Passing an integer after the ':' will cause that field to be a minimum number of characters wide
"""
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

for x in range(1, 11):
    print(f'{x:2d} {x*x:3d} {x*x*x:4d}')

f=open(("json_dump.json"),"w")

json.dump([1, 'simple', 'list'],f)

x = json.load(f)

f.close()

print(x)
