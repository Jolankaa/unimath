# Poyraz Soylu
# unimath
# analysis functions

from functools import reduce
import operator
from definitions.set import Mset
from core.parse import ParseMset
from sets import Bool_Natural,Bool_RealNumber


def sigmanotation(i: int , n:int , func) -> int:
    """
    Σ (Sigma Notation) - Summation

    Calculates the sum of a sequence of terms from start to end.
    This function generalizes the idea of summation using a custom function.

    Parameters:
        func (callable): A function f(i) that defines the terms of the sequence.
        i (int): The starting index (inclusive).
        n (int): The ending index (inclusive).

    Returns:
        int or float: The sum of f(i) for i in [i,n].

    Example:
        >>> sigmanotation(lambda i: i, 1, 5)
        15  # (1 + 2 + 3 + 4 + 5)

        >>> sigmanotation(lambda k: k**2, 1, 4)
        30  # (1^2 + 2^2 + 3^2 + 4^2)
    """
    for i in range(i,n + 1):
        values = list()
        values.append(func(i))

        return sum(values)


def productnatation(i: int, n:int , func) -> int:
    """
    Π (Product Notation) - Multiplication of terms

    Calculates the product of a sequence of terms from start to end.
    This function generalizes the idea of multiplication using a custom function.

    Parameters:
        func (callable): A function f(i) that defines the terms of the sequence.
        i (int): The starting index (inclusive).
        n (int): The ending index (inclusive).

    Returns:
        int or float: The product of f(i) for i in [i,n].

    Example:
        >>> productnatation(lambda i: i, 1, 4)
        24  # (1 * 2 * 3 * 4)

        >>> productnatation(lambda k: k/(k+1), 1, 3)
        0.25  # (1/2 * 2/3 * 3/4)
    """
    return reduce(operator.mul, (func(i) for i in range(i, n + 1)), 1)

def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer n.

    Factorial (n!) is the product of all positive integers from 1 to n.
    It is widely used in combinatorics, probability, and algebra.

    Formula:
        n! = n * (n-1) * (n-2) * ... * 1
        0! = 1 (by definition)

    Parameters:
        n (int): A non-negative integer

    Returns:
        int: The factorial of n

    Raises:
        ValueError: If n is negative
    """
    try:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    except ValueError:
        print("[ERROR] Factorial is not defined for negative numbers.")

def Transformation(rule , domain ):
    parsed = ParseMset(str(domain))

    NLowLimit = parsed.get("Lowlimit", None)
    NHighLimit = parsed.get("HighLimit", None)
    NLowOpenRange = parsed["LowOpenRange"]
    NHighOpenRange = parsed["HighOpenRange"]
    NExcluded = parsed["Excluded"]

    return Mset(
        rule(float(NLowLimit)),
        rule(float(NHighLimit)),
        NLowOpenRange,
        NHighOpenRange,
        NExcluded
    )

def series(rule, n):


    """
    All well-defined functions from natural numbers to real numbers are called series.

    Parameters :
        rule : general term of the series
        n : serieses index for a wanteed

    Examples :
        >>> (a)n is a serie . rule is 1/n
            for n = 1
                return 1/1
            for n = 2
                return 1/2
    """
    if Bool_Natural(n) == True and Bool_RealNumber(rule(n)) == True:
        return rule(n)
    else:
        from errors import NonCompliancaRecognition
        NonCompliancaRecognition()

def Sum_Series(rule , endpoint):
    """
    It is a function that provides the sum of the elements in the series.

    Example: 
        >>> (a)n = 1/n:
            endpoint: 3
            1/1 + 1/2 + 1/3  = 11/3 

    """
    sum_prod = list()
    for i in range(1,endpoint):
        sum_prod.append(rule(i))
    
    return sum(sum_prod)

def CharacteristicSeries(rule , n=10_000):
    """
    It is a function that understands the monotonicity of the series
    and the characteristic of the series and returns it.
    """
    
    differences = list()
    differences = []
    ratios = []
    values = []

    for i in range(n):
        values.append(rule(i))

    for i in range(1, len(values)):
        differences.append(values[i] - values[i-1])
        if values[i-1] != 0:
            ratios.append(values[i] / values[i-1])

    if all(d > 0 for d in differences):
            monotony = "Increasing Series"
    elif all(d < 0 for d in differences):
            monotony = "Decreasing Series"
    elif all(d == 0 for d in differences):
            monotony = "Constant Series"
    else:
            monotony = "Non-monotonic Series"

    if len(set(round(d, 6) for d in differences)) == 1:
        typeofseries = "Arithmetic Series"
    elif len(set(round(r, 6) for r in ratios)) == 1:
        typeofseries = "Geometric Series"
    else:
        typeofseries = "Other / Unknown Type"

    return monotony, typeofseries