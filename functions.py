def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


f = fib
f(100)

# since, the function doesn't return anything, therefore by default, it returns None
print(f(10))


# Default Argument Value function
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# Default arguments
# ask_ok('Do you really want to quit?')

# can also be used using keyword argument
ask_ok('OK to overwrite the file?', retries=2, reminder='Come on, only yes or no!')


# WARNING : Default value is evaluated only once
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))

# Special Parameter
"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
"""


def pos_only_arg(arg, /):
    print(arg)


def keyword_only_arg(*, arg):
    print(arg)


def combine(pos_only, / , standard , * , kwd_only):
    print(pos_only,standard,kwd_only)


pos_only_arg(1)
# pos_only_arg(arg=1) - not possible

# keyword_only_arg(1) - not possible since it uses keyword argument
keyword_only_arg(arg=3)

"""
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given
"""
combine(1, 2, kwd_only=3)

# standard can be positional or keyword here
combine(1, standard=2, kwd_only=3)

"""
>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got an unexpected keyword argument 'pos_only'
"""