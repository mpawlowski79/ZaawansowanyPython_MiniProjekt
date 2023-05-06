class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vector2D(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("Nieobsługiwany operand dla +")

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
print(v1 + v2) 
print(v1 + (5, 6))
print((7, 8) + v2)
