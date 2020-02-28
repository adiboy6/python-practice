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
