# sembolik ifadeler için işlem ysapmaya olanak sağlayan sınıf ve fonksiyonlar 


class symbol:
    def __init__(self, sym, coefficient=1, scaler=None):
        if isinstance(sym , str):
            self.sym = sym
        else:
            raise TypeError("sembol tanıma uygun değil")
        if isinstance(coefficient , int):
            self.coefficient = coefficient
        else:
            raise TypeError("sembol tanıma uygun değil")
        if isinstance(scaler , (int,float)):
            self.scaler = scaler 
        
    def __add__(self, other):
            if isinstance(other, symbol) and self.sym == other.sym:
                return symbol(self.sym, self.coefficient + other.coefficient)
            else:
                raise ValueError("Sadece aynı semboller birbiriyle toplanabilir.")
    
    def __sub__(self, other):
        if isinstance(other, symbol) and self.sym == other.sym:
            return symbol(self.sym, self.coefficient - other.coefficient)

    def __repr__(self):
        return f"{self.coefficient if self.coefficient != 1 else ''}{self.sym}"
t = symbol("t")
n = symbol("n")
print(n+n-t)