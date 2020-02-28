"""
the innermost scope, which is searched first, contains the local names

the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names

the next-to-last scope contains the current module’s global names

the outermost scope (searched last) is the namespace containing built-in names

"""

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        # The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
