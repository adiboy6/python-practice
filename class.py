class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


a = Dog("Boxer")
b = Dog("Bulldog")

print(a.kind)
print(b.kind)

a.kind = "Canine"

print(a.kind)
print(b.kind)

print(a.name)
print(b.name)

def f1(self, x, y):
    return min(x, x + y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

c = C()
print(c.f(1, 2))  # Calls f1 method
print(c.g())      # Calls g method