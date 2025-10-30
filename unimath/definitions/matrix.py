from errors import NonCompliancaRecognition


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def __repr__(self):
        return "\n".join(["  ".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            NonCompliancaRecognition()
            print("To perform addition operations on matrices, the number of rows and columns must be equal.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    
    @staticmethod
    def PrimeDiagonal(data):
        for i in range(1, len(data)):       
            for j in range(1, len(data[i])):
                pass
    
    def Matrixİdentifier(self, data):
        """
        Specifies the definition of the matrix. A special matrix shows its properties.

        Examples:
            >>> [[0,0],[0,0]]
            definiton : square matris rows : 2 , cols : 2
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

        Data_Property = list()

        if self.rows == self.cols :
            Data_Property.append("Square Matrix")




    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Çarpma için sütun/satır boyutları uyumlu olmalı")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                   for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)
    
if __name__ == "__main__":
    NonCompliancaRecognition()