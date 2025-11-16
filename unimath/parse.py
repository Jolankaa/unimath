#the file used to perform the parse operation


import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from unimath.mset import Mset

def ParseMset(s):
    """
    ParseMset:
    This function parses the defined set.

    Parametres:
    s : defined set

    """
    s = s.strip().replace(" ", "") 
    
    range_part, *excluded_part = s.split("-")
    
    LowOpenRange = range_part.startswith("(")
    HighOpenRange = range_part.endswith(")")
    
    range_numbers = range_part[1:-1].split(",")
    LowLimit = float(range_numbers[0])
    HighLimit = float(range_numbers[1])
    
    if excluded_part:
        excluded_str = excluded_part[0].strip("{}")
        excluded = set(map(float, excluded_str.split(",")))
    else:
        excluded = set()
    
    return {
        "LowLimit": LowLimit,
        "HighLimit": HighLimit,
        "LowOpenRange": LowOpenRange,
        "HighOpenRange": HighOpenRange,
        "Excluded": excluded
    }
