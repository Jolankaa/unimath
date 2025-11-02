from errors import NonCompliancaRecognition
import math

class Vector:
    def __init__(self, dimensions):
        if not isinstance(dimensions , list) :
            raise TypeError("You must list the dimensions for manipulation")
        if not 1<len(dimensions)<=3:
            raise ValueError("The vectors you define can be 2 or 3 dimensional")
        self.dimensions = dimensions

    def magnitude(self):
        """
        function to find the magnitude of the vector
        """
        if len(self.dimensions) == 2:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            length = (x**2 + y**2)**0.5

        elif len(self.dimensions) == 3:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            z = self.dimensions[2]
            length = (x**2 + y**2 + z**2)**1/2
        return length

    def information(self):
        """
        This function returns the information of the defined vector.
        """
        vektorinformation = [

        ]
        if len(self.dimensions) == 2:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            vektorinformation.append({"dimension":2 })
            length = (x**2 + y**2)**0.5
            vektorinformation.append(length)

        elif len(self.dimensions) == 3:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            z = self.dimensions[2]
            vektorinformation.append({"dimension":2})
            length = (x**2 + y**2 + z**2)**1/2
            vektorinformation.append({"length":length})    
        return vektorinformation
    
    def Inner_product(self, other):
        """
        This function finds the inner product of two defined vectors.
        """

        if len(self.dimensions) != len(other.dimensions):
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a*b for a, b in zip(self.dimensions, other.dimensions))
    
    def AngleTwoVector(self, other):
        """
        It is a function that finds the angle between two vectors according to the inner product equation.
        """
        if len(self.dimensions) != len(other.dimensions):
            raise ValueError("Vectors must have the same dimension for dot product.")

        inner_product = self.Inner_product(other)
        mag1 = self.magnitude()
        mag2 = other.magnitude()

        cos_theta = max(-1, min(1, inner_product / (mag1 * mag2)))

        return math.acos(cos_theta)

    def __repr__(self):
        return f"Vector({self.dimensions})"

    def __str__(self):
        if len(self.dimensions) == 2:
            dimensions = "R^2"
        elif len(self.dimensions) == 3:
            dimensions = "R^3"

        return f"<Vector {self.dimensions}, |v|={self.magnitude():.2f} , dimensions={dimensions}>"
        
    def __add__(self, other):
        """Vector addition"""
        if len(self.dimensions) != len(other.dimensions):
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector([a + b for a, b in zip(self.dimensions, other.dimensions)])

    def __sub__(self, other):
        """Vector subtraction"""
        if len(self.dimensions) != len(other.dimensions):
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector([a - b for a, b in zip(self.dimensions, other.dimensions)])

    def __mul__(self, scalar):
        """Scalar multiplication"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("You can only multiply a vector by a scalar (number).")
        return Vector([a * scalar for a in self.dimensions])

    def __matmul__(self, other):
        """Dot product with @ operator"""
        return self.Inner_product(other)

    def __eq__(self, other):
        """Check if two vectors are equal"""
        return self.dimensions == other.dimensions
    
    def __getitem__(self, index):
        return self.dimensions[index]

    def __iter__(self):
        return iter(self.dimensions)
