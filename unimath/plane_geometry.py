from errors import NonCompliancaRecognition
import math

class vector:
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

        
        
