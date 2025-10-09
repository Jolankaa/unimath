from errors import NonCompliancaRecognition
from itertools import count 
from definitions.set import Mset


def FiniteCrateSet(i,n,k) -> list:

    """
    This function allows you to create a cluster

    Parametres:
        i : start value 
        n : stop value 
        k : multiples 

    Examples: 
        i = 1 , n = 14 , k = 2
        {2,4,6,8,10,12,14}
    
    """
    for j in range(i,n+1):
        sets = list()
        if j % k == 0 :
            sets.append(j)
    return sets

def Natural():
    """
    ℕ :
    This function represents the set of natural numbers.
    According to Peano's axioms and ours, 0 is not included.
    
    This function continues to translate until it cannot be stopped under the required conditions.

    {1,2,3,...}
    """

    Naturals = Mset(1,"inf",LowOpenRange=False ,HighOpenRange=False , Excluded=None)
    
    return Naturals

        
def Bool_Natural(n: int) -> bool:
    """
    ℕ :
       This function checks whether the parameter is a natural number.
    
    Return:
        True , False
    """

    if n >= 1 and n.is_integer() == True:
        return True
    else:
        False

def Bool_Integer(n:int): 
    """
    ℤ:
        This function checks whether the parameter is an integer.
    Return:
        True , False
    """
    
    return n.is_integer()

def Integer(n: int) :
    """
    ℤ:
    This function contains the set of integers defined by mathematics.
    The set of integers is not a countably infinite set.

    {..., -2, -1, 0, 1, 2, ...}
    """
    n = 0
    yield n
    step = 1
    while True:
        yield step
        yield -step
        step += 1

