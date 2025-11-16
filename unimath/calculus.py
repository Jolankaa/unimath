# Poyraz Soylu
# unimath
# analysis functions

from functools import reduce
import operator


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

"""def Transformation(rule , domain ):
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
    )"""
