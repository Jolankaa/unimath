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
            raise DefinitionError("For the aggregation to be defined, the number of rows and columns must be the same.")

    def __repr__(self):
        return "\n".join(str(row) for row in self.arrays)

A = Matrix([
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
])
