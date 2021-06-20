#Implementation of chaining in python

class TestHash:
    def __init__(self, b):
        self.BOX = b                            # b = box length
        self.table = [[] for x in range(b)]

    def insert(self, x):
        i = x % self.BOX
        self.table[i].append(x)

    def remove(self, x):
        i = x % self.BOX
        if x in self.table[i]:
            self.table[i].remove(x)

    def search(self, x):
        i = x % self.BOX
        return x in self.table[i]


h = TestHash(7)

#Insertion-Deletion-searching operation in hash-table

h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
print(h.search(56))
h.remove(56)
