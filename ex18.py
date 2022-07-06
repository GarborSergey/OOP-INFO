# ==================== __getitem__, __setitem__, __delitem__ =======================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        if 0 <= item < len(self.marks ):
            return self.marks[item]
        else:
            raise IndexError('Index error')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Index must be positive int')

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Index must be positive int')

        del self.marks[key]

s1 = Student('Alex', [5, 5, 5, 2, 3, 4])
s1[10] = 4
del s1[10]
print(s1.marks)