class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Addition
    def __add__(self, c2):
        return Complex(
            self.real + c2.real,
            self.imag + c2.imag
        )

    # Multiplication
    def __mul__(self, c2):
        real = self.real * c2.real - self.imag * c2.imag
        imag = self.real * c2.imag + self.imag * c2.real
        return Complex(real, imag)

    # String representation
    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)
print(c1 * c2)