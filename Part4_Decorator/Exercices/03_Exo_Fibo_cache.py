import typing 

"""
Cette classe fonction pour une fonction factoriel qui n'est pas récursive
"""
class Memorize:
    cache = 0
    pos = 0

    def __init__(self, f):
        self.f = f

    def __call__(self, *t, **v):
        n, = t
        if Memorize.cache > 0:
            # print(Memorize.cache, Memorize.pos)
            res = Memorize.cache * self.f(n, Memorize.pos)
            Memorize.pos = n
            Memorize.cache  = res
            
            return res
            
        Memorize.pos = n 
        Memorize.cache = self.f(*t, **v)

        return Memorize.N 

@Memorize
def factoriel(n: int , end: int = 0)-> int:
    res = 1
    while n > end:
        res *= n
        n = n - 1
    
    return res