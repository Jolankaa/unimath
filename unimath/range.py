# for sup and inf function
 
from unimath.mset import Mset
from parse import ParseMset

def sup(set: Mset) -> Mset:

    parsed = set.ParseMset(set)

    NLowLimit = parsed.get("Lowlimit", None)
    NLowOpenRange = parsed["LowOpenRange"]


    if NLowOpenRange == False and NLowOpenRange == True:
        return NLowLimit
    

def inf(set: Mset) -> Mset:

    parsed = set.ParseMset(set)

    NHighLimit = parsed.get("HighLimit", None)
    NHighOpenRange = parsed["HighOpenRange"]


    if NHighOpenRange == False and NHighOpenRange == True :
        return NHighLimit

