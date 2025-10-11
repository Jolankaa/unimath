from calculus import factorial
from errors import NonCompliancaRecognition 

def permutation(repetetion:str, n:int, r:int) ->int :    
    """
    In mathematics, a permutation of a set can mean one of two different things:

    an arrangement of its members in a sequence or linear order, or
    the act or process of changing the linear order of an ordered set.

    Formula: 
        if repetetion is 1 = n!/(n-r)!
        receptions is 0 = n^r

    Parameters:
        repetetion(int)= whether the permutation is repeated or not
        n(int)
        r(int)

    Return:
        return a permutation of given values
    """
        #terms
    if n>=r:
        pass
    else:
        print("[ERROR] Does not fit this description")
        exit()

    if repetetion == "0":
        return factorial(n)/factorial(n - r)
    elif repetetion == "1":
        return n**r
    
    
def combination(n: int, r: int) -> int: 
    """
    In mathematics,
    a combination is a selection of items from a set that has distinct members,
    such that the order of selection does not matter

    Formula: 
        c(n,r) = n!/r!(n-r)!

    Parametres:
        n(int)
        r(int)
    
    Return:
        return a combination of given values

    """
    #terms
    if n>=r:
        pass
    elif n == r:
        return 1
    else:
        NonCompliancaRecognition()

    return factorial(n)/factorial(r)*factorial(n - r)

def posibilty(n:int , r: int) -> int:
    """
    Probability is a branch of mathematics and statistics concerning events and numerical
    descriptions of how likely they are to occur.
    The probability of an event is a number between 0 and 1;
    the larger the probability, the more likely an event is to occur.

    Formula:
        
    """
    if r == 0 and n>r :
        NonCompliancaRecognition()
    
    return n/r

