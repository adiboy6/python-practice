"""
    range(stop):
        Starts from 0 to stop - 1
    range(start,stop[,step]):
        Starts from start to stop - 1 with an incremental step(positive) or decremental step(negative)

    it behaves like a list but it isn't
"""
r = range(0, 20, 2)

print(11 in r)
print(10 in r)

print(r[5])

# shows the first 5 elements range
print(r[:5])
