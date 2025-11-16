#This file allows you to define data types that do not exist in Python.


class Mset:
    def __init__(self, LowLimit=None , HighLimit=None, LowOpenRange=False ,HighOpenRange= False, Excluded=None):

        """
        This class defines the set mathematically.
        """
        
        self.LowLimit = LowLimit
        self.HighLimit = HighLimit
        self.LowOpenRange = LowOpenRange
        self.HighOpenRange = HighOpenRange
        self.Excluded = set(Excluded or [])

    def __contains__(self, x):
        if self.LowLimit is not None:
            if self.LowOpenRange and x <= self.LowLimit:
                return False
            if not self.LowOpenRange and x < self.LowLimit:
                return False
        
        if self.HighLimit is not None:
            if self.HighOpenRange and x >= self.HighLimit:
                return False
            if not self.LowOpenRange and x > self.HighLimit:
                return False

        if x in self.Excluded:
            return False

        return True
    
    @staticmethod
    def from_string(s):
        s = s.strip().replace(" ", "")  
        
        range_part, *excluded_part = s.split("-")
        
        acik_alt = range_part.startswith("(")
        acik_ust = range_part.endswith(")")
        
        range_numbers = range_part[1:-1].split(",")
        alt = float(range_numbers[0])
        ust = float(range_numbers[1])
        
        if excluded_part:
            excluded_str = excluded_part[0].strip("{}")
            excluded = set(map(float, excluded_str.split(","))) if excluded_str else set()
        else:
            excluded = set()

        return Mset(alt, ust, acik_alt, acik_ust, excluded)

    def __repr__(self):

        low = "(" if self.LowOpenRange else "["
        high = ")" if self.HighOpenRange else "]"
        if self.Excluded == None:
            return f"{low}{self.LowLimit}, {self.HighLimit}{high}"
        else:
            return f"{low}{self.LowLimit}, {self.HighLimit}{high} - {{{', '.join(map(str, sorted(self.Excluded)))}}}"