from errors import * 


class Matrix:
    """
    In mathematics,
    a matrix is a rectangular array of numbers or other mathematical objects
    with elements or entries arranged in rows and columns,
    usually satisfying certain properties of addition and multiplication.
    """
    def __init__(self, arrays):

        if not arrays: 
            raise DefinitionError("Data Cannot Be Empty") 
        if not isinstance(arrays, list) or not all(isinstance(row, list) for row in arrays):
            raise DefinitionError("İncorrectly Defined")
        
        self.arrays = arrays
        self.rows = len(arrays)

        try:
            self.cols = len(arrays[0])
            if not all(len(row) == self.cols for row in arrays):
                raise DefinitionError("Incorrectly Defined")
        except IndexError:
            raise DefinitionError("indentation cannot be empty. Did you mean ?: zero matrix")
        
    def get_column(self, index):
        """Returns the specified column as a list."""
        if index < 0 or index >= self.cols:
            raise IndexError("Column index out of range.")
        return [row[index] for row in self.arrays]
    
    def DelColumn(self, index): 
        """
        Allows to delete the column indexed in the given parameter
        """
        result = [
            
        ]
        pass

    def Transpose(self):
        """
        This function transposes the matrix.
        """
        """
        cols = [self.get_column(i) for i in range(self.cols)]
        return Matrix(cols)
        """
        transposed_data = [
            [self.arrays[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]
        return Matrix(transposed_data)
    
    def is_SquareMatrix(self):
        """
        A square matrix is a matrix with the same number of rows and columns. 
        It occupies an important place, 
        especially in the definition of determinants
        """

        if self.rows == self.cols:
            return True 
        else: 
            return False
        
    def is_SymmetricalMatrix(self):
        """
            A matrix is symmetrical if it is equal to its transpose. A == Aᵗ
        """
        if self.is_SquareMatrix == False:
            return False
    
        transposed = self.Transpose()
        if self == transposed:
            return True
        
    """def Cofactor(self, rows , cols):
        first_product = (-1)**(rows+cols)

        cofactor_matris = 

        second_product = 
        


        pass"""
        
    def Determinant(self):
        """
        In mathematics, the determinant is a scalar-valued function of the entries of a square matrix.
        The determinant of a matrix A is commonly denoted det(A),
        det A, or |A|. Its value characterizes some properties of the matrix and the linear map represented, 
        on a given basis, by the matrix.
        """

        if self.is_SquareMatrix() == False:
            raise DefinitionError("The determinant is defined in square matrices")
        try:
            if self.FindDimension() == (2,2):
                value = self.FindElement(1,1)*self.FindElement(2,2) - self.FindElement(1,2)*self.FindElement(2,1)
                return value
            
            if self.FindDimension() == (3,3):
                """
                sarrus method
                """
                right = (
                self.FindElement(1,1)*self.FindElement(2,2)*self.FindElement(3,3)+
                self.FindElement(2,1)*self.FindElement(3,2)*self.FindElement(1,3)+
                self.FindElement(3,1)*self.FindElement(1,2)*self.FindElement(2,3)
                )

                left = (
                self.FindElement(3,1)*self.FindElement(2,2)*self.FindElement(1,3)+
                self.FindElement(2,3)*self.FindElement(3,2)*self.FindElement(1,1)+
                self.FindElement(3,3)*self.FindElement(1,2)*self.FindElement(2,1)
                )

                return right + left
        except TypeError:
            raise NonSymbolicValue("This determinant function can only calculate on numeric data. For symbolic data, please refer to the SymbolicMatrix function.")


    def FindElement(self, row, cols):
        """
        It allows to find the element in the desired column and row.
        """
        try:
            result = self.arrays[row-1][cols-1]
        except IndexError:
            raise DefinitionError("More value were entered than the number of rows or columns in the matrix.")

        return result
    
    def FindDimension(self):
        """
        Returns the dimensions of the input matrix

        Example: 
            >>> Matrix.FindDimension(1,2)
                search (a)1,2
                and finding in matrix

        """
        return (self.rows ,self.cols)


    def __matmul__(self,other):
        """
        classic row-by-column and column-by-row multiplication
        """
        if not self.cols == self.rows:
            raise DefinitionError("In order to multiply two matrices (A@B), the number of columns of matrix A must be equal to the number of rows of matrix B.")
    
        result = [[0 for _ in range(len(other.arrays[0]))] for _ in range(len(self.arrays))]

        for i in range(len(self.arrays)):         
            for j in range(len(other.arrays[0])):   
                for k in range(len(other.arrays)):  
                    result[i][j] += self.arrays[i][k] * other.arrays[k][j]

        return Matrix(result)

    def __mul__(self , other):
        """
        Hadamard product 
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise DefinitionError("The number of rows and columns of two matrices must be equal")
        
        try:
            result = [
                [self.arrays[i][j] * other.arrays[i][j] for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(result)
        except IndexError:
            raise DefinitionError("wrong index defined")
        



    """  
    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("The number of rows and columns in the matrix must be the same")
        for i in 
    """


    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.arrays[i][j] != other.arrays[i][j]:
                    return False
        return True

    def __add__(self, other):
        """
        Necessary definitions and operations for matrix addition
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("The number of rows and columns in the matrix must be the same")

        try:
            result = [
                [self.arrays[i][j] + other.arrays[i][j] for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(result)
        except IndexError:
            raise DefinitionError("For the aggregation to be defined, the number of rows and columns must be the same.")

    def __sub__(self ,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("The number of rows and columns in the matrix must be the same")

        try:
            result = [
                [self.arrays[i][j] - other.arrays[i][j] for j in range(self.cols)]
                for i in range(self.rows)
            ]
            return Matrix(result)
        except IndexError:
            raise DefinitionError("For the subregation to be defined, the number of rows and columns must be the same.")

    def __repr__(self):
        return "\n".join(str(row) for row in self.arrays)

"""A = Matrix([
    [1, 2, 3],
    [2, 5, 5],
    [2, 5, "n"]
])

print(A.Determinant())"""
