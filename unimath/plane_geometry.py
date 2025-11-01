from errors import NonCompliancaRecognition

class vector:
    def __init__(self, dimensions):
        if not isinstance(dimensions , list) :
            raise TypeError("You must list the dimensions for manipulation")
        if not 1<len(dimensions)<=3:
            raise ValueError("The vectors you define can be 2 or 3 dimensional")
        self.dimensions = dimensions

    def information(self):
        vektorinformation = [

        ]
        if len(self.dimensions) == 2:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            vektorinformation.append({"dimension":2 })
            length = (x**2 + y**2)**1/2
            vektorinformation.append(length)

        elif len(self.dimensions) == 3:
            x = self.dimensions[0] 
            y = self.dimensions[1]
            z = self.dimensions[2]
            vektorinformation.append(dimension = "3")
            length = (x**2 + y**2 + z**2)**1/2
            vektorinformation.append({"length":length})    
        return vektorinformation
    
    def Inner_product(self, other):
        if len(self.dimensions) != len(other.dimensions):
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a*b for a, b in zip(self.dimensions, other.dimensions))
        


        
        
