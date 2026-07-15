class Vector:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self, other):
        return Vector ( 
        self.x + other.x,
        self.y + other.y,
        self.z + other.z
        )

    def __mul__(self, other):
        return (
        self.x * other.x +
        self.y * other.y +
        self.z * other.z 
        )
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k "
    
c =  Vector(1,2,3)
c1 = Vector(4,5,6)
c2 = Vector(7,8,90)

print(c + c1)
print(c + c2)
print(c *c1)

