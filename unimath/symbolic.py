from .errors import RequiredModule


try:
    from sympy import symbols, Function, simplify, Matrix as SymMatrix
except ModuleNotFoundError:
    raise RequiredModule("The unimath library works integrated with sympy to perform symbolic operations, so we use sympy in functions that require symbolic operations.")



class SymbolicVariable:
    """
    Sembolik değişkenleri temsil eder. Örn: n, k, x
    """
    def __init__(self, name: str):
        self.symbol = symbols(name)

    def __repr__(self):
        return f"SymbolicVariable({self.symbol})"


class SymbolicExpression:
    """
    Her türlü sembolik ifadeyi taşır.
    Toplama, çıkarma, çarpma gibi işlemler overload edilmiştir.
    """
    def __init__(self, expr):
        self.expr = expr

    def simplify(self):
        return SymbolicExpression(simplify(self.expr))

    def __add__(self, other):
        return SymbolicExpression(self.expr + other.expr)

    def __sub__(self, other):
        return SymbolicExpression(self.expr - other.expr)

    def __mul__(self, other):
        return SymbolicExpression(self.expr * other.expr)

    def __truediv__(self, other):
        return SymbolicExpression(self.expr / other.expr)

    def __repr__(self):
        return f"SymbolicExpression({self.expr})"


class Sequence:
    """
    Sembolik diziler (a_n) oluşturmak için.
    rule: lambda n: ifade
    """
    def __init__(self, rule):
        self.rule = rule
        self.n = symbols("n", integer=True)

    def term(self, k: int):
        return self.rule(k)

    def symbolic_term(self):
        return self.rule(self.n)
    
    def monotony(self):
        """
        the basic rule of monotony:
        >>> (a)n+1 - (a)n > 0 -> increasing
        >>> (a)n+1 - (a)n < 0 -> decreasing
        >>> (a)n+1 - (a)n = 0 -> constant
        """
        
        if simplify(self.rule(self.n+1)/self.rule(self.n)) > 1:
            return "increasing"
        if simplify(self.rule(self.n+1)/self.rule(self.n)) < 1:
            return "decreasing"
        if simplify(self.rule(self.n+1)/self.rule(self.n)) == 1:
            return "constant"


class SymbolicMatrix:
    """
    Normal matris sınıfınıza sembolik destek için bir wrapper.
    """
    def __init__(self, data):
        self.data = data
        self.matrix = SymMatrix(data)

    def determinant(self):
        return simplify(self.matrix.det())

    def transpose(self):
        return SymbolicMatrix(self.matrix.T.tolist())

    def __repr__(self):
        return f"SymbolicMatrix({self.matrix})"
