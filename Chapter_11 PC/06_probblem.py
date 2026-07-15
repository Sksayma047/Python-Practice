class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Vector Addition
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    # Dot Product
    def __mul__(self, other):
        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2) #Output: Vector(5,7,9)
print(v1 * v2) #Output: 32

print(v1 + v3) #Output: Vector(8,10,12)
print(v1 * v3) #Output: 50



# __init__() → Object banne par automatically chalta hai.
# __add__() → + operator ka behavior define karta hai.
# __mul__() → * operator ka behavior define karta hai.
# __str__() → print(object) karne par object ko readable string me convert karta hai.